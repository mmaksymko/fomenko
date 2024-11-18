from repository.attempt_repository import AttemptRepository


class AttemptService:
    def __init__(self):
        self.attempt_repository = AttemptRepository()
        
    def get_all_attempts(self):
        return self.attempt_repository.get_all_attempts()
    
    def get_all_attempts_for_course(self, course_id):
        return self.attempt_repository.get_all_attempts_for_course(course_id)

    def get_all_course_attempts_for_student(self, student_id, course_id):
        return self.attempt_repository.get_all_course_attempts_for_student(student_id, course_id)

    def get_all_attempts_for_student(self, student_id):
        return self.attempt_repository.get_all_attempts_for_student(student_id)
    
    def get_all_attempts_for_task(self, task_id):
        return self.attempt_repository.get_all_attempts_for_task(task_id)
    
    def get_total_attempts_for_task(self, tasks, task_id, student_id):
        return self.attempt_repository.get_total_attempts_for_task(tasks, task_id, student_id)
    
    def get_succesful_attempts_for_task(self, tasks, student_id):
        return self.attempt_repository.get_succesful_attempts_for_task(tasks, student_id)