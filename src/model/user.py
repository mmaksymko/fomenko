from model import db
from sqlalchemy import Column, Integer, String, Enum as SQLAlchemyEnum, Text
from sqlalchemy.orm import relationship
from enum import Enum as PythonEnum

# Define the UserRole Enum using the standard Python Enum
class UserRole(PythonEnum):
    student = "student"
    editor = "editor"
    admin = "admin"

class User(db.Model):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    role = Column(SQLAlchemyEnum(UserRole), nullable=False)
    entry_year = Column(Integer, nullable=False)
    group_number = Column(Integer, nullable=False)
    speciality_shortened = Column(String(100), nullable=False)
    profile_pic = Column(Text, nullable=True)
    
    attempts = relationship('Attempt', backref='user')
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role.value,
            'entry_year': self.entry_year,
            'group_number': self.group_number,
            'speciality_shortened': self.speciality_shortened,
            'profile_pic': self.profile_pic,
            'attempts': [attempt.to_dict() for attempt in self.attempts]
        }