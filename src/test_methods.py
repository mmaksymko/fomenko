import os
import sys
import unittest
from datetime import datetime, timezone
from model import db
from model.user import User
from model.user_course import UserCourse
from model.course import Course
from model.task import Task
from model.attempt import Attempt
from service.grade_service import GradeService
from service.task_analysis_service import TaskAnalysisService
from service.user_service import UserService
from service.prediction_service import PredictionService
from flask import Flask

class TestMethods(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()
            self.populate_test_data()

    def populate_test_data(self):
        user1 = User(id=1, first_name='John', last_name='Doe', role='student', entry_year=2020, group_number=1, speciality_shortened='CS')
        user2 = User(id=2, first_name='Jane', last_name='Smith', role='student', entry_year=2021, group_number=2, speciality_shortened='CS')
        task1 = Task(id=1, course_id=1, name='Task 1', deadline=datetime.now(timezone.utc), max_attempts=3, max_score=100, pass_score=50)
        task2 = Task(id=2, course_id=1, name='Task 2', deadline=datetime.now(timezone.utc), max_attempts=3, max_score=100, pass_score=50)
        course1 = Course(id=1, name='Course 1')
        course2 = Course(id=2, name='Course 2')
        userCourse1 = UserCourse(student_id = 1, course_id = 1)
        userCourse2 = UserCourse(student_id = 1, course_id = 2)
        attempt1 = Attempt(id=1, student_id=1, task_id=1, grade=80, date_start=datetime.now(timezone.utc), date_finish=datetime.now(timezone.utc))
        attempt2 = Attempt(id=2, student_id=1, task_id=2, grade=90, date_start=datetime.now(timezone.utc), date_finish=datetime.now(timezone.utc))
        attempt3 = Attempt(id=3, student_id=2, task_id=1, grade=70, date_start=datetime.now(timezone.utc), date_finish=datetime.now(timezone.utc))
        db.session.add_all([user1, user2, task1, task2, course1, course2, userCourse1, userCourse2, attempt1, attempt2, attempt3])
        db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_attempt_to_dict(self):
        with self.app.app_context():
            attempt = db.session.get(Attempt, 1)
            expected_dict = {
                'id': 1,
                'student_id': 1,
                'task_id': 1,
                'grade': 80,
                'date_start': attempt.date_start,
                'date_finish': attempt.date_finish
            }
            self.assertEqual(attempt.to_dict(), expected_dict)

    def test_calculate_average_grade(self):
        with self.app.app_context():
            grade_service = GradeService()
            avg_grade = grade_service.calculate_average_grade(1, 1)
            self.assertEqual(avg_grade, 80)

    def test_calculate_total_score(self):
        with self.app.app_context():
            grade_service = GradeService()
            total_score = grade_service.calculate_total_score(1, 1)
            self.assertEqual(total_score, 80)

    def test_get_grades_for_course(self):
        with self.app.app_context():
            grade_service = GradeService()
            grades = grade_service.get_grades_for_course(1)
            self.assertEqual(len(grades), 2)

    def test_get_users(self):
        with self.app.app_context():
            user_service = UserService()
            users = user_service.get_users(course_id=1)
            self.assertEqual(len(users), 1)

    def test_calculate_completion_percentage(self):
        with self.app.app_context():
            task_analysis_service = TaskAnalysisService()
            completion_percentage = task_analysis_service.calculate_completion_percentage()
            self.assertEqual(len(completion_percentage), 2)

    def test_get_attempts_success_ratio(self):
        with self.app.app_context():
            task_analysis_service = TaskAnalysisService()
            success_ratio = task_analysis_service.get_attempts_success_ratio()
            self.assertEqual(len(success_ratio), 2)

    def test_get_course_feedback(self):
        with self.app.app_context():
            task_analysis_service = TaskAnalysisService()
            feedback = task_analysis_service.get_course_feedback(1)
            self.assertEqual(feedback.course_id, 1)

    def test_get_average_grades_for_all_users(self):
        with self.app.app_context():
            grade_service = GradeService()
            average_grades = grade_service.get_average_grades_for_all_users()
            self.assertEqual(len(average_grades), 2)

    def test_get_total_scores_for_all_users(self):
        with self.app.app_context():
            grade_service = GradeService()
            total_scores = grade_service.get_total_scores_for_all_users()
            self.assertEqual(len(total_scores), 2)

    def test_get_courses_feedback(self):
        with self.app.app_context():
            task_analysis_service = TaskAnalysisService()
            feedbacks = task_analysis_service.get_courses_feedback()
            self.assertGreaterEqual(len(feedbacks), 0)

if __name__ == '__main__':
    unittest.main()