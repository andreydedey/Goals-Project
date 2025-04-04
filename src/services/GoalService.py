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

        user_id = goal_data.get("user_id")
        print(user_id)

        # Checking if user really exists
        user = self.__user_repository.getUser(user_id)
        print(user)
        if not user:
            return jsonify({"response": "No user Found"}), 404

        goal = self.__goals_repository.insertGoal(goal_data)

        return jsonify({"goal": goal}), 201

    def get_week_pending_goals(self):
        goals = self.__goals_repository.getWeekPendingGoals()

        return jsonify({"pending_goals": goals}), 200

    def get_week_completed_goals(self):
        goals = self.__goals_repository.getWeekCompletedGoals()

        return jsonify({"completed_goals": goals}), 200
