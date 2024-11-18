from model import db
from sqlalchemy import Column, Integer, ForeignKey
from model.user import User
from model.course import Course

class UserCourse(db.Model):
    __tablename__ = 'user_course'
    
    student_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    course_id = Column(Integer, ForeignKey(Course.id), primary_key=True)