from typing import TypedDict

from src.models.repository.GoalsRepository import GoalsRepository


class RegistryData(TypedDict):
    title: str
    desiredFrequency: int


class GoalService:
    def __init__(self) -> None:
        self.__goals_repository = GoalsRepository()

    def create_goal(self, data: RegistryData) -> int:
        print(data)

        # There is suposed to have some logic here !
        goal = self.__goals_repository.insertGoal(data)

        return {"goal": "Goal teste"}
