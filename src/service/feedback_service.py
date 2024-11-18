from repository.feedback_repository import FeedbackRepository


class FeedbackService:
    def __init__(self):
        self.feedback_repository = FeedbackRepository()
        
    def get_all_feedback(self):
        return self.feedback_repository.get_all_feedback()
    
    def get_all_feedback_for_course(self, course_id):
        return self.feedback_repository.get_all_feedback_for_course(course_id)