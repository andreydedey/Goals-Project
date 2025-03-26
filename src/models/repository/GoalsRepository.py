from typing import Dict

from sqlalchemy.exc import NoResultFound

from src.models.entities.Goal import Goal
from src.models.config.connection import db_connection_handler


class GoalsRepository:
    def getGoal(self, goal_id: str):
        with db_connection_handler as database:
            try:
                goal = (
                    database.session.query(Goal)
                    .filter(goal_id == Goal.id)
                    .with_entities(Goal.title, Goal.desiredWeekFrequency, Goal.creationDate, Goal.description, Goal.user_id)
                    .one()
                )
                return goal
            except NoResultFound:
                return None


    def insertGoal(self, goal_data: Dict) -> Goal:
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
    

    def getWeekPendingGoals(self, goal_id):
        with db_connection_handler as database:
            try:
                # Consulta difícil, devo ver 
                pass
                # goals = (
                #     database.session.query(Goal)
                #     .
                # )
            except Exception as error:
                database.session.rollback()
                return error
