from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.sql import func
from src.models.config.base import Base


class GoalCompletion(Base):
    __tablename__ = "goal_completion"

    id = Column(String, primary_key=True)
    completion_date = Column(DateTime, default=func.now())
    goal_id = Column(String, ForeignKey("goal.id"))
