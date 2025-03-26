from uuid import uuid4

from src.models.repository.UserRepository import UserRepository

class UserService:
    def __init__(self) -> None:
        self.__user_repository = UserRepository()

    def register_user(self, user_data) -> int:
        print(user_data)

        # Creat id
        user_data["uuid"] = str(uuid4())

        user = self.__user_repository.registerUser(user_data)

        return {"body": user, "status_code": 201}
