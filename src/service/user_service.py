from model.attempt import Attempt
from model.user import User
from model.user_course import UserCourse
from repository.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
    
    def get_users(self, course_id=None, grade=None, group_number=None, entry_year=None, speciality_shortened=None, sort_by=None, order='asc'):
        return self.user_repository.get_users(course_id, grade, group_number, entry_year, speciality_shortened, sort_by, order)
    
    def get_all_users_by_role(self, role: str):
        return self.user_repository.get_all_users_by_role(role)
    
    def get_user_by_id(self, user_id: int):
        return self.user_repository.get_user_by_id(user_id)
    