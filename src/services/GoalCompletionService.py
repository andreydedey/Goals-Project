from uuid import uuid4

from flask import jsonify

from src.models.repository.GoalCompletionRepository import GoalCompletionRepository
from src.models.repository.GoalRepository import GoalRepository


class GoalCompletionService:
    def __init__(self) -> None:
        self.__goal_completion_repository = GoalCompletionRepository()
        self.__goal_repository = GoalRepository()

    def create_goal_completion(self, goal_completion_data) -> int:
        # Gerando ID
        goal_completion_data["id"] = str(uuid4())

        goal_id = goal_completion_data.get("goal_id")
        goal = self.__goal_repository.getGoal(goal_id)

        if not goal:
            print("No goal Found")
            return jsonify({"body": "No Goal found"}), 404

        goal_completion = self.__goal_completion_repository.insertGoalCompletion(
            goal_completion_data
        )
        print(goal_completion)

        return {"body": goal_completion, "status_code": 201}
