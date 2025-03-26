from typing import Dict

from src.models.entities.Goal import Goal
from src.models.config.connection import db_connection_handler


class GoalsRepository:
    def insertGoal(self, goal_info: Dict) -> Goal:
        with db_connection_handler as database:
            try:
                goal = Goal(
                    id=goal_info.get("uuid"),
                    title=goal_info.get("title"),
                    desiredWeekFrequency=goal_info.get("desiredWeekFrequency"),
                    description=goal_info.get("description"),
                    id_usuario=goal_info.get("id_usuario"),
                )

                database.session.add(goal)
                database.session.commit()

                return goal
            except Exception as error:
                database.session.rollback()
                print(error)
