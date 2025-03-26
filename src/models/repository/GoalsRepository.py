from typing import Dict

from sqlalchemy.exc import NoResultFound

from src.models.entities.Goal import Goal
from src.models.config.connection import db_connection_handler


class GoalsRepository:
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
