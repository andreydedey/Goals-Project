from typing import Dict

from sqlalchemy.exc import NoResultFound

from src.models.entities.User import User
from src.models.config.connection import db_connection_handler


class UserRepository:
    def registerUser(self, user_info: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                user = User(
                    id=user_info.get("uuid"),
                    name=user_info.get("name"),
                    email=user_info.get("email"),
                    password=user_info.get("password"),
                )

                database.session.add(user)
                database.session.commit()

                return user_info
            except Exception as error:
                database.session.rollback()
                return {"body": error, "status_code": 500}

    def getUser(self, user_id: str) -> User:
        with db_connection_handler as database:
            try:
                user = (
                    database.session.query(User)
                    .filter(user_id == User.id)
                    .with_entities(User.name, User.email, User.password)
                    .one()
                )

                return user
            except NoResultFound:
                return None
