from model.attempt import Attempt
from model.task import Task
from model.user import User
from model.course import Course
from dto.grade_course_response import GradeCourseResponse
from dto.grade_response import GradeResponse
from service.attempt_service import AttemptService
from service.course_service import CourseService
from service.task_service import TaskService
from service.user_service import UserService

class GradeService:
    def __init__(self):
        self.user_service = UserService()
        self.task_service = TaskService()
        self.attempt_service = AttemptService()
        self.course_service = CourseService()

    
    def get_grades_for_course(self, course_id):
        # Query all attempts for the specified course
        attempts = self.attempt_service.get_all_attempts_for_course(course_id)
        
        # Prepare a dictionary to hold the result in the desired structure
        result = []

        # Iterate over each attempt to extract user and task data
        for attempt in attempts:
            # Fetch the user and task related to the attempt
            user = self.user_service.get_user_by_id(attempt.student_id)
            task = self.task_service.get_task_by_id(attempt.task_id)

            # Check if the user already exists in the result list
            user_dto = next((item for item in result if item.user_id == user.id), None)

            if not user_dto:
                # If the user doesn't exist in the result list, create a new user DTO
                user_dto = GradeResponse(
                    user_id=user.id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    grades=[]
                )
                result.append(user_dto)

            # Check if the task already exists in the user's task list in the DTO
            task_dto = next((task_item for task_item in user_dto.grades if task_item['task_id'] == task.id), None)

            if not task_dto:
                # If the task doesn't exist, create a new task DTO with the score
                task_dto = {
                    'task_id': task.id,
                    'task_name': task.name,
                    'scores': [attempt.grade]
                }
                user_dto.grades.append(task_dto)
            else:
                # If the task already exists, just append the grade to the existing scores list
                task_dto['scores'].append(attempt.grades)

        # Convert DTOs to dictionary format and return the result
        return [dto.__dict__ for dto in result]
    
    def calculate_average_grade(self, student_id, course_id):
        attempts = self.attempt_service.get_all_course_attempts_for_student(student_id, course_id)
        return sum(attempt.grade for attempt in attempts) / len(attempts) if attempts else 0

    def calculate_total_score(self, student_id, course_id):
        attempts = self.attempt_service.get_all_course_attempts_for_student(student_id, course_id)
        return sum(attempt.grade for attempt in attempts)
    
    def get_average_grades_for_all_users(self):
        result = []
        
        # Query all users
        users = self.user_service.get_all_users_by_role('student')
        # Query all courses once
        courses = self.course_service.get_all_courses()

        for user in users:
            # Initialize a GradeResponse for each user
            user_response = GradeCourseResponse(user_id=user.id, first_name=user.first_name, last_name=user.last_name)
            
            # Iterate over all courses to calculate the average grade
            for course in courses:
                # Calculate the average grade for this user in this course
                avg_grade = self.calculate_average_grade(user.id, course.id)
                # If the user has no attempts, avg_grade will be None; set to "No attempts" instead
                user_response.add_course(course.id, course.name, avg_grade if avg_grade is not None else "No attempts")
            
            # Append the populated user response to the result
            result.append(user_response.__dict__)

        return result

    def get_total_scores_for_all_users(self):
        result = []
        
        # Query all users
        users = self.user_service.get_all_users_by_role('student')
        # Query all courses once
        courses = self.course_service.get_all_courses()

        for user in users:
            # Initialize a GradeResponse for each user
            user_response = GradeCourseResponse(user_id=user.id, first_name=user.first_name, last_name=user.last_name)
            
            # Iterate over all courses to calculate the total score
            for course in courses:
                # Calculate the total score for this user in this course
                total_score = self.calculate_total_score(user.id, course.id)
                # If the user has no attempts, total_score will be None; set to "No attempts" instead
                user_response.add_course(course.id, course.name, total_score if total_score is not None else "No attempts")
            
            # Append the populated user response to the result
            result.append(user_response.__dict__)

        return result
