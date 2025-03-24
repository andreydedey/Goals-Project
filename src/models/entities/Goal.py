from sqlalchemy import Column, DateTime, String, Text, Integer
from sqlalchemy.sql import func
from src.models.config.base import Base


class Goal(Base):
    __tablename__ = "goal"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    desiredWeekFrequency = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)
    creationDate = Column(DateTime, default=func.now())
    id_usuario = Column(Integer, nullable=True)

    def __repr__(self):
        return f"Goal [title={self.title}, description={self.description}, creationDate={self.creationDate}, completionDate={self.completionDate}]"
