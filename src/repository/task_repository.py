from model.task import Task


class TaskRepository:
    def get_task_by_id(id):
        return Task.query.get(id)
    
    def get_all_task_by_course(course_id):
        return Task.query.filter_by(course_id=course_id).all()