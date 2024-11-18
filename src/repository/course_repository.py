from model.course import Course
from model.task import Task


class CourseRepository:
    def get_all_courses():
        return Course.query.all()
    
    def get_course_by_id(id):
        return Course.query.get(id)
    
    def get_course_by_task_id(task_id):
        return Course.query.join(Task).filter(Task.id == task_id).first()