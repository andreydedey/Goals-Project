from flask import Blueprint, request, jsonify

from src.services.UserService import UserService

user_route_bp = Blueprint("user", __name__, url_prefix="/user")


@user_route_bp.route("register_user", methods=["POST"])
def register_user_route():
    try:
        user_service = UserService()

        response = user_service.register_user(user_data=request.json)
        print(response)
        return jsonify(response)
    except Exception as error:
        print(error)
        return jsonify({"error": error}), 500
