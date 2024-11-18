from model.feedback import Feedback


class FeedbackRepository:
    def get_all_feedback():
        return Feedback.query.all()
    
    def get_all_feedback_for_course(course_id):
        return Feedback.query.filter_by(course_id=course_id).all()