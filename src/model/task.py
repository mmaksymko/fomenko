from datetime import datetime
from model import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime, timedelta, timezone

from model.course import Course

def two_weeks_from_now():
    return datetime.now(timezone.utc) + timedelta(weeks=2)

class Task(db.Model):
    __tablename__ = 'task'
    
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey(Course.id), nullable=False)
    name = Column(String(100), nullable=True)
    deadline = Column(DateTime, default=two_weeks_from_now, nullable=False)
    max_attempts = Column(Integer, nullable=False)
    max_score = Column(Integer, nullable=False)
    pass_score = Column(Integer, nullable=False)