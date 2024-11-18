from typing import List, Optional
from dto.attempt_response import AttemptResponse

class CourseCorrelationResponse:
    def __init__(self, course_id: int, course_name: str, attempts: List[AttemptResponse], correlation: Optional[float]):
        self.course_id = course_id
        self.course_name = course_name
        self.attempts = attempts
        self.correlation = correlation
        
    def to_dict(self):
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'attempts': [attempt.to_dict() for attempt in self.attempts],
            'correlation': self.correlation
        }