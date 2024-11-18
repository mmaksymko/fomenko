from abc import ABC, abstractmethod

class PredictionStrategy(ABC):
    @abstractmethod
    def predict(self, student_id, course_id=None, start_date=None, end_date=None):
        pass