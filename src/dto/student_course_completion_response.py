from typing import List
from dto.course_correlation_response import CourseCorrelationResponse

class StudentCourseCompletionResponse:
    def __init__(self, student_id: int, first_name: str, last_name: str, courses: List[CourseCorrelationResponse]):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.courses = courses
        
    def to_dict(self):
        return {
            'student_id': self.student_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'courses': [course.to_dict() for course in self.courses]
        }