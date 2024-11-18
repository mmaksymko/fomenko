class CourseSuccessRatioResponse:
    def __init__(self, course_id: int, course_name: str, total_attempts: int, successful_tasks: int):
        self.course_id = course_id
        self.course_name = course_name
        self.total_attempts = total_attempts
        self.successful_tasks = successful_tasks
        
    def to_dict(self):
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'total_attempts': self.total_attempts,
            'successful_tasks': self.successful_tasks
        }