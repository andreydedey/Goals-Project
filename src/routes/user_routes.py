from flask import Blueprint, request, jsonify

from src.services.UserService import UserService

user_route_bp = Blueprint("user", __name__, url_prefix="/user")


@user_route_bp.route("register_user", methods=["POST"])
def register_user_route():
    try:
        user_service = UserService()

        response = user_service.register_user(user_data=request.json)
        return response
    except Exception as error:
        return jsonify({"error": error}), 500
