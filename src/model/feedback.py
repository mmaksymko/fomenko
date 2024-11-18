from model import db
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from model.course import Course
from model.user import User

class Feedback(db.Model):
    __tablename__ = 'feedback'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey(User.id), nullable=False)
    course_id = Column(Integer, ForeignKey(Course.id), nullable=False)
    comment = Column(String(500), nullable=True)
    rating = Column(Integer, CheckConstraint('rating >= 1 AND rating <= 5'), nullable=False)
    date = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    
    student = relationship("User", backref="feedbacks")
    course = relationship("Course", backref="feedbacks")