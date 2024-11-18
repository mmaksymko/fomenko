from model.attempt import Attempt
from model.task import Task


class AttemptRepository:
    def get_all_attempts():
        return Attempt.query.all()
    
    def get_all_attempts_for_course(course_id):
        return Attempt.query.join(Task).filter(Task.course_id == course_id).all()
    
    def get_all_course_attempts_for_student(student_id, course_id):
        return Attempt.query.join(Task).filter(Task.course_id == course_id and Attempt.student_id == student_id).all()
    
    def get_all_attempts_for_student(student_id):
        return Attempt.query.filter_by(student_id=student_id).all()
    
    def get_all_attempts_for_task(task_id):
        return Attempt.query.filter_by(task_id=task_id).all()
    
    def get_total_attempts_for_task(tasks, task_id, student_id):
        return sum(
                Attempt.query.filter_by(task_id=task.id, **({"student_id": student_id} if student_id else {})).count()
                for task in tasks
            )
    def get_succesful_attempts_for_task(tasks, student_id):
        return sum(
                1 for task in tasks
                if Attempt.query.filter_by(task_id=task.id, **({"student_id": student_id} if student_id else {}))
                .filter(Attempt.grade >= task.pass_score)
                .first()
            )