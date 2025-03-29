from flask import Blueprint, request, jsonify

from src.services.GoalService import GoalService

goal_route_bp = Blueprint("goal", __name__, url_prefix="/goal")


@goal_route_bp.route("create_goal", methods=["POST"])
def create_goal_route():
    goal_service = GoalService()

    response = goal_service.create_goal(goal_data=request.json)
    return response


@goal_route_bp.route("get_week_pending_goals", methods=["GET"])
def get_week_pending_goals_route():
    goal_service = GoalService()

    response = goal_service.get_week_pending_goals()
    return response


@goal_route_bp.route("get_week_completed_goals", methods=["GET"])
def get_week_completed_goals_route():
    goal_service = GoalService()

    response = goal_service.get_week_completed_goals()
    return response