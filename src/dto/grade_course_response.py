class GradeCourseResponse:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []

    def add_course(self, course_id, task_name, grade):
        self.courses.append({
            'course': course_id,
            'task_name': task_name,
            'grade': grade
        })

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'courses': self.courses
        }
