class AttemptResponse:
    def __init__(self, score: float, time_taken: float):
        self.score = score
        self.time_taken = time_taken
        
    def to_dict(self):
        return {
            'score': self.score,
            'time_taken': self.time_taken
        }