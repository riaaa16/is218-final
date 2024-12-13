'''SQLAlchemy model for storing attacks in the database'''
from datetime import datetime, timezone
import uuid
from sqlalchemy import Column, String, Integer, Float, CheckConstraint, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase

# All mapped classes inherit from this base class
class Base(DeclarativeBase):
    '''Base class for SQLAlchemy ORM models.'''

# SQLAlchemy Attack model
class Attack(Base):
    '''Model for attacks'''
    __tablename__ = 'attacks'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    sender = Column(String(50), nullable=False)
    recipient = Column(String(50), nullable=False)
    team = Column(String(4), nullable=False)
    link = Column(String(2000), nullable=False)
    finish = Column(Float, nullable=False)
    color = Column(Float, nullable=False)
    shading = Column(Float, nullable=False)
    bg = Column(Float, nullable=False)
    size = Column(Float, nullable=False)
    num_chars = Column(Integer, CheckConstraint('num_chars > 0'), nullable=False)
    score = Column(Float, nullable=False)

    def __repr__(self):
        '''String representation for debugging and logging'''
        return (
            f"sender = {self.sender}\n"
            f"recipient = {self.recipient}\n"
            f"team = {self.team}\n"
            f"link = {self.link}\n"
            f"finish = {self.finish}\n"
            f"color = {self.color}\n"
            f"shading = {self.shading}\n"
            f"bg = {self.bg}\n"
            f"size = {self.size}\n"
            f"num_chars = {self.num_chars}\n"
            f"score = {self.score}"
        )
