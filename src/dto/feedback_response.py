class FeedbackResponse:
    def __init__(self, user_id: int, first_name: str, last_name: str, score: float, comment: str):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.score = score
        self.comment = comment
        
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'score': self.score,
            'comment': self.comment
        }