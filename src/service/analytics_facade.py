from service.grade_service import GradeService
from service.prediction_service import PredictionService
from service.task_analysis_service import TaskAnalysisService
from service.prediction_strategy.prediction_strategy import PredictionStrategy
from service.user_service import UserService

class AnalyticsFacade:
    def __init__(self):
        self.grade_service = GradeService()
        self.prediction_service = PredictionService()
        self.task_analysis_service = TaskAnalysisService()
        self.user_service = UserService()

    def get_average_grade(self, student_id, course_id):
        return self.grade_service.calculate_average_grade(student_id, course_id)

    def get_average_grades_for_all_users(self):
        return self.grade_service.get_average_grades_for_all_users()

    def get_total_score(self, student_id, course_id):
        return self.grade_service.calculate_total_score(student_id, course_id)
    
    def get_total_scores_for_all_users(self):
        return self.grade_service.get_total_scores_for_all_users()

    def predict_grade(self, student_id, course_id=None, strategy = "date", start_date=None, end_date=None):
        return self.prediction_service.predict_grades(strategy, student_id, course_id, start_date, end_date)

    def calculate_score_time_correlation(self):
        return self.task_analysis_service.calculate_score_time_correlation()

    def calculate_completion_percentage(self):
        return self.task_analysis_service.calculate_completion_percentage()

    def get_attempts_success_ratio(self):
        return self.task_analysis_service.get_attempts_success_ratio()

    def get_users(self, course_id=None, grade=None, group_number=None, entry_year=None, speciality_shortened=None, sort_by=None, order='asc'):
        return self.user_service.get_users(course_id, grade, group_number, entry_year, speciality_shortened, sort_by, order)

    def get_grades_for_course(self, course_id):
        return self.grade_service.get_grades_for_course(course_id)
    
    def get_course_feedback(self, course_id):
        return self.task_analysis_service.get_course_feedback(course_id)
    
    def get_courses_feedback(self):
        return self.task_analysis_service.get_courses_feedback()