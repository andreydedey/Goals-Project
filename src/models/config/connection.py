from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models.config.base import Base

# Load the environment variables
load_dotenv()

# .env variables
pghost = os.getenv("PGHOST")
pgdatabase = os.getenv("PGDATABASE")
pguser = os.getenv("PGUSER")
pgpassword = os.getenv("PGPASSWORD")


class __DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = (
            f"postgresql://{pguser}:{pgpassword}@{pghost}/{pgdatabase}"
        )
        self.__engine = None
        self.session = None

    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__connection_string)

        # Create tables
        Base.metadata.create_all(bind=self.__engine)

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


db_connection_handler = __DBConnectionHandler()
