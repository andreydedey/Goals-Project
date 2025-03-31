from src.models.entities.GoalCompletion import GoalCompletion
from src.models.config.connection import db_connection_handler


class GoalCompletionRepository:
    def insertGoalCompletion(self, goal_completion_data):
        with db_connection_handler as database:
            try:
                goal_completion = GoalCompletion(
                    id=goal_completion_data.get("id"),
                    goal_id=goal_completion_data.get("goal_id"),
                )
                database.session.add(goal_completion)
                database.session.commit()

                return goal_completion_data
            except Exception as error:
                database.session.rollback()
