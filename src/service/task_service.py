from repository.task_repository import TaskRepository

class TaskService:
    def __init__(self):
        self.task_repository = TaskRepository()
        
    def get_task_by_id(self, id):
        return self.task_repository.get_task_by_id(id)
    
    def get_all_task_by_course(self, course_id):
        return self.task_repository.get_all_task_by_course(course_id)
