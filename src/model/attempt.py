from datetime import datetime, timezone
from model import db
from sqlalchemy import Column, DateTime, Integer, Float, ForeignKey, CheckConstraint
from model.user import User
from model.task import Task

class Attempt(db.Model):
  __tablename__ = 'attempt'
  
  id = Column(Integer, primary_key=True)
  student_id = Column(Integer, ForeignKey(User.id), nullable=False)
  task_id = Column(Integer, ForeignKey(Task.id), nullable=False)
  grade = Column(Float, CheckConstraint('grade >= 0'), nullable=False)
  date_start = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
  date_finish = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
  
  def to_dict(self):
    return {
      'id': self.id,
      'student_id': self.student_id,
      'task_id': self.task_id,
      'grade': self.grade,
      'date_start': self.date_start,
      'date_finish': self.date_finish
    }
    