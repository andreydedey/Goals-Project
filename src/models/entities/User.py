from sqlalchemy import Column, DateTime, ForeignKey, String
from src.models.config.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"User [name={self.name}, email={self.email}, password={self.password}]"
