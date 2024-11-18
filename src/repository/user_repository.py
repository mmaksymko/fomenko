from model.attempt import Attempt
from model.user import User
from model.user_course import UserCourse


class UserRepository:
    def get_users(self, course_id=None, grade=None, group_number=None, entry_year=None, speciality_shortened=None, sort_by=None, order='asc'):
        query = User.query
        
        if course_id:
            query = query.join(UserCourse).filter(UserCourse.course_id == course_id)
        if grade:
            query = query.join(Attempt).filter(Attempt.grade >= grade)
        if group_number:
            query = query.filter(User.group_number == group_number)
        if entry_year:
            query = query.filter(User.entry_year == entry_year)
        if speciality_shortened:
            query = query.filter(User.speciality_shortened == speciality_shortened)
        
        if sort_by:
            attr = getattr(User, sort_by)
            query = query.order_by(attr)
            result = query.all()
            if order == 'desc':
                result = result[::-1]
        else:
            result = query.all()

        return result
    
    def get_all_users_by_role(role: str):
       User.query.filter_by(role=role).all()
    
    def get_user_by_id(user_id: int):
        return User.query.get(user_id)