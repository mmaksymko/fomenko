from sklearn.linear_model import LinearRegression
import numpy as np
from model.attempt import Attempt
from model.task import Task
from service.attempt_service import AttemptService
from service.prediction_strategy.prediction_strategy import PredictionStrategy
from service.task_service import TaskService

class CourseBasedPredictionStrategy(PredictionStrategy):
    def __init__(self):
        self.task_service = TaskService()
        self.attempt_service = AttemptService()
        
    def predict(self, student_id, course_id, start_date=None, end_date=None):
        tasks = self.task_service.get_all_task_by_course(course_id)
        if not tasks:
            return 0

        total_max_score = sum(task.max_score for task in tasks)
        if total_max_score == 0:
            return 0

        # Get all attempts for the student in the course
        attempts = self.attempt_service.get_all_course_attempts_for_student(student_id, course_id)
        
        total_score = sum(attempt.grade for attempt in attempts)
        predicted_score = (total_score / total_max_score) * 100

        return min(predicted_score, 100)