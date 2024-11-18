from model import db
from sqlalchemy import Column, Integer, String

class Course(db.Model):
    __tablename__ = 'course'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
