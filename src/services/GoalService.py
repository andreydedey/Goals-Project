from uuid import uuid4

from src.models.repository.GoalsRepository import GoalsRepository

class GoalService:
    def __init__(self) -> None:
        self.__goals_repository = GoalsRepository()

    def create_goal(self, goal_data) -> int:
        print(goal_data)

        # Gerando uuid
        goal_data["uuid"] = str(uuid4()) 

        # There is suposed to have some logic here !
        goal = self.__goals_repository.insertGoal(goal_data)

        return {"body": goal, "status_code": 201}
