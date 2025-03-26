from uuid import uuid4

from src.models.repository.GoalCompletionRepository import GoalCompletionRepository

class GoalCompletionService:
    def __init__(self) -> None:
        self.__goal_completion_repository = GoalCompletionRepository()

    def create_goal_completion(self, data) -> int:
        print(data)

        goal_completion = self.__goal_completion_repository.insertGoalCompletion(data)

        return {"body": goal_completion, "status_code": 201}

