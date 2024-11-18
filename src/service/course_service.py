from repository.course_repository import CourseRepository


class CourseService:
    def __init__(self):
        self.course_repository = CourseRepository()
        
    def get_all_courses(self):
        return self.course_repository.get_all_courses()
    
    def get_course_by_id(self, id):
        return self.course_repository.get_course_by_id(id)
    
    def get_course_by_task_id(self, task_id):
        return self.course_repository.get_course_by_task_id(task_id)