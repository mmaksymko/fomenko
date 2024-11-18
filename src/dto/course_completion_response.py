class CourseCompletionResponse:
    def __init__(self, course_id: int, course_name: str, completed_tasks: int, total_tasks: int, completion_percentage: float):
        self.course_id = course_id
        self.course_name = course_name
        self.completed_tasks = completed_tasks
        self.total_tasks = total_tasks
        self.completion_percentage = completion_percentage

    def to_dict(self):
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'completed_tasks': self.completed_tasks,
            'total_tasks': self.total_tasks,
            'completion_percentage': self.completion_percentage
        }