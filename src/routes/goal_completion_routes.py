from flask import Blueprint, request

from src.services.GoalCompletionService import GoalCompletionService

goal_completion_route_bp = Blueprint("goal_completion", __name__, url_prefix="/goal_completion")


@goal_completion_route_bp.route("create_goal_completion", methods=["POST"])
def create_goal_completion_route():
    goal_completion_service = GoalCompletionService()

    response = goal_completion_service.create_goal_completion(goal_completion_data=request.json)
    return response
