from flask import Blueprint, request, jsonify

from src.services.GoalService import GoalService

goal_route_bp = Blueprint("goal", __name__, url_prefix="/goal")


@goal_route_bp.route("create_goal", methods=["POST"])
def create_goal():
    try:
        goal_service = GoalService()

        response = goal_service.create_goal(goal_info=request.json)
        print(response)
        return jsonify(response)
    except Exception as error:
        print(error)
        return jsonify({"error": error}), 500
