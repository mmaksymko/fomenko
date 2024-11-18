from model.task import Task
from model.attempt import Attempt
from model.feedback import Feedback
from model.user import User
from model.course import Course
from scipy.stats import pearsonr

from dto.course_correlation_response import CourseCorrelationResponse
from dto.student_course_completion_response import StudentCourseCompletionResponse
from dto.attempt_response import AttemptResponse
from dto.course_completion_response import CourseCompletionResponse
from dto.feedback_response import FeedbackResponse
from dto.course_feedback_response import CourseFeedbackResponse
from dto.course_success_ratio_response import CourseSuccessRatioResponse
from service.attempt_service import AttemptService
from service.course_service import CourseService
from service.feedback_service import FeedbackService
from service.task_service import TaskService
from service.user_service import UserService

class TaskAnalysisService:
    def __init__(self):
        self.user_service = UserService()
        self.task_service = TaskService()
        self.attempt_service = AttemptService()
        self.feedback_service = FeedbackService()
        self.course_service = CourseService()
    
    def calculate_score_time_correlation(self):
        attempts = self.attempt_service.get_all_attempts()
        result = {}
        
        for attempt in attempts:
            course = self.course_service.get_course_by_task_id(attempt.task_id)
            if course:
                course_id = course.id
                course_name = course.name
                if course_id not in result:
                    result[course_id] = {
                        'course_id': course_id,
                        'course_name': course_name,
                        'attempts': [],
                        'correlation': None
                    }
                time_taken = (attempt.date_finish - attempt.date_start).total_seconds() / 60
                result[course_id]['attempts'].append({
                    'score': attempt.grade,
                    'time_taken': time_taken
                })

        for course_id, course_data in result.items():
            scores = [attempt['score'] for attempt in course_data['attempts']]
            times_taken = [attempt['time_taken'] for attempt in course_data['attempts']]
            if len(scores) > 1 and len(times_taken) > 1:
                correlation, _ = pearsonr(scores, times_taken)
                course_data['correlation'] = correlation
            else:
                course_data['correlation'] = None

        return [CourseCorrelationResponse(
            course_id=course_data['course_id'],
            course_name=course_data['course_name'],
            attempts=[AttemptResponse(score=attempt['score'], time_taken=attempt['time_taken']) for attempt in course_data['attempts']],
            correlation=course_data['correlation']
        ) for course_data in result.values()]

    def calculate_completion_percentage(self):
        courses = self.course_service.get_all_courses()
        if not courses:
            return []

        result = {}

        for course in courses:
            tasks = self.task_service.get_all_task_by_course(course.id)
            for task in tasks:
                attempts = self.attempt_service.get_all_attempts_for_task(task.id)
                for attempt in attempts:
                    student_id = attempt.student_id
                    student = self.user_service.get_user_by_id(student_id)
                    if student_id not in result:
                        result[student_id] = {
                            'student_id': student_id,
                            'first_name': student.first_name,
                            'last_name': student.last_name,
                            'courses': {}
                        }
                    if course.id not in result[student_id]['courses']:
                        result[student_id]['courses'][course.id] = {
                            'course_id': course.id,
                            'course_name': course.name,
                            'completed_tasks': 0,
                            'total_tasks': 0
                        }
                    result[student_id]['courses'][course.id]['total_tasks'] += 1
                    if attempt.grade >= task.pass_score:
                        result[student_id]['courses'][course.id]['completed_tasks'] += 1

        for student_id, student_data in result.items():
            for course_id, course_data in student_data['courses'].items():
                course_data['completion_percentage'] = (course_data['completed_tasks'] / course_data['total_tasks']) * 100
            student_data['courses'] = list(student_data['courses'].values())

        return [StudentCourseCompletionResponse(
            student_id=student_data['student_id'],
            first_name=student_data['first_name'],
            last_name=student_data['last_name'],
            courses=[CourseCompletionResponse(
                course_id=course['course_id'],
                course_name=course['course_name'],
                completed_tasks=course['completed_tasks'],
                total_tasks=course['total_tasks'],
                completion_percentage=course['completion_percentage']
            ) for course in student_data['courses']]
        ) for student_data in result.values()]

    def get_courses_feedback(self):
        feedback_records = self.feedback_service.get_all_feedback()
        return [self.get_course_feedback(feedback.course_id) for feedback in feedback_records]

    def get_course_feedback(self, course_id):
        feedback_records = self.feedback_service.get_all_feedback_for_course(course_id)
        course = self.course_service.get_course_by_id(course_id)
        course_name = course.name if course else "Unknown Course"

        course_entry = {
            'course_id': course_id,
            'course_name': course_name,
            'feedbacks': []
        }

        for feedback in feedback_records:
            user = self.user_service.get_user_by_id(feedback.student_id)
            course_entry['feedbacks'].append({
                'user': {
                    'id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                },
                'score': feedback.rating,
                'comment': feedback.comment
            })

        return CourseFeedbackResponse(
            course_id=course_entry['course_id'],
            course_name=course_entry['course_name'],
            feedbacks=[FeedbackResponse(
                user_id=feedback['user']['id'],
                first_name=feedback['user']['first_name'],
                last_name=feedback['user']['last_name'],
                score=feedback['score'],
                comment=feedback['comment']
            ) for feedback in course_entry['feedbacks']]
        )

    def get_attempts_success_ratio(self, student_id=None):
        courses = self.course_service.get_all_courses()
        if not courses:
            return []

        result = []

        for course in courses:
            tasks = self.task_service.get_all_task_by_course(course.id)
            total_attempts = self.attempt_service.get_total_attempts_for_task(tasks, student_id)
            successful_tasks = self.attempt_service.get_succesful_attempts_for_task(tasks, student_id)
            result.append({
                "course_id": course.id,
                "course_name": course.name,
                "total_attempts": total_attempts,
                "successful_tasks": successful_tasks
            })

        return [CourseSuccessRatioResponse(
            course_id=course['course_id'],
            course_name=course['course_name'],
            total_attempts=course['total_attempts'],
            successful_tasks=course['successful_tasks']
        ) for course in result]