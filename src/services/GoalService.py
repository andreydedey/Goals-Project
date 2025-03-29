from uuid import uuid4

from flask import jsonify

from src.models.repository.GoalRepository import GoalRepository
from src.models.repository.UserRepository import UserRepository

class GoalService:
    def __init__(self) -> None:
        self.__goals_repository = GoalRepository()
        self.__user_repository = UserRepository()


    def create_goal(self, goal_data):
        # Gerando uuid
        goal_data["uuid"] = str(uuid4()) 

        # Checking if user really exists
        user = self.__user_repository.getUser(goal_data.get("user_id"))
        if not user:
            return jsonify({"body": "No user Found"}), 404

        goal = self.__goals_repository.insertGoal(goal_data)
        print(goal)

        return jsonify({"body": goal}), 201


    def get_week_pending_goals(self):
        goals = self.__goals_repository.getWeekPendingGoals()

        return jsonify({"body": goals}), 200