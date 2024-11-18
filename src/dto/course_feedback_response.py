from typing import List
from dto.feedback_response import FeedbackResponse

class CourseFeedbackResponse:
    def __init__(self, course_id: int, course_name: str, feedbacks: List[FeedbackResponse]):
        self.course_id = course_id
        self.course_name = course_name
        self.feedbacks = feedbacks
        
    def to_dict(self):
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'feedbacks': [feedback.to_dict() for feedback in self.feedbacks]
        }