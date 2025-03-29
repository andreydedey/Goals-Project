import arrow
from datetime import datetime

from sqlalchemy.exc import NoResultFound
from sqlalchemy import select, func

from src.models.entities.Goal import Goal
from src.models.entities.GoalCompletion import GoalCompletion

from src.models.config.connection import db_connection_handler


class GoalRepository:
    def getGoal(self, goal_id: str):
        with db_connection_handler as database:
            try:
                goal = (
                    database.session.query(Goal)
                    .filter(goal_id == Goal.id)
                    .with_entities(
                        Goal.title,
                        Goal.desiredWeekFrequency,
                        Goal.creationDate,
                        Goal.description,
                        Goal.user_id,
                    )
                    .one()
                )
                return goal
            except NoResultFound:
                return None

    def insertGoal(self, goal_data) -> Goal:
        with db_connection_handler as database:
            try:
                goal = Goal(
                    id=goal_data.get("uuid"),
                    title=goal_data.get("title"),
                    desiredWeekFrequency=goal_data.get("desiredWeekFrequency"),
                    description=goal_data.get("description"),
                    user_id=goal_data.get("user_id"),
                )

                database.session.add(goal)
                database.session.commit()

                return goal_data

            except Exception as error:
                database.session.rollback()
                return error

    def getWeekPendingGoals(self):
        now = arrow.now()

        week_start = now.floor("week").datetime
        week_end = now.ceil("week").datetime

        with db_connection_handler as database:
            try:
                week_pending_goals = (
                    database.session.execute(
                        select(
                            Goal.id,
                            Goal.title,
                            Goal.desiredWeekFrequency,
                            func.count(GoalCompletion.id).label(
                                "goalCompletionWeekCount"
                            ),  # Contagem de completion
                        )
                        .outerjoin(GoalCompletion)
                        .where(
                            GoalCompletion.completion_date.between(week_start, week_end)
                        )
                        .group_by(Goal.id)
                        .having(
                            func.count(GoalCompletion.id) < Goal.desiredWeekFrequency
                        )
                    )
                ).all()

                week_pending_goals_dict = [row._asdict() for row in week_pending_goals]

                return week_pending_goals_dict

            except Exception as error:
                return error


    def getWeekCompletedGoals(self):
            now = arrow.now()

            week_start = now.floor("week").datetime
            week_end = now.ceil("week").datetime

            with db_connection_handler as database:
                try:
                    week_completed_goals = (
                        database.session.execute(
                            select(
                                Goal.id,
                                Goal.title,
                                Goal.desiredWeekFrequency,
                                func.count(GoalCompletion.id).label(
                                    "goalCompletionWeekCount"
                                ),  # Contagem de completion
                            )
                            .outerjoin(GoalCompletion)
                            .where(
                                GoalCompletion.completion_date.between(week_start, week_end)
                            )
                            .group_by(Goal.id)
                            .having(
                                func.count(GoalCompletion.id) >= Goal.desiredWeekFrequency
                            )
                        )
                    ).all()

                    week_completed_goals_dict = [row._asdict() for row in week_completed_goals]

                    return week_completed_goals_dict

                except Exception as error:
                    return error
