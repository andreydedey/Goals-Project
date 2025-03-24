from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.sql import func
from src.models.config.base import Base


class Goal(Base):
    __tablename__ = "goal"

    id = Column(String, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    goal_id = Column(String, nullable=False)
