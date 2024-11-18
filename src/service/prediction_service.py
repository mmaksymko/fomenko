from service.prediction_strategy.prediction_strategy import PredictionStrategy
from service.prediction_strategy.prediction_factory import PredictionFactory
from datetime import datetime

class PredictionService:
    def __init__(self):
        self.factory = PredictionFactory()
    
    def predict_grades(
        self,
        strategy: str,
        student_id: int,
        course_id: int = None | int,
        start_date: datetime = None | datetime,
        end_date: datetime = None | datetime
    ):
        strategy: PredictionStrategy = self.factory.get_prediction_strategy(course_id, start_date, end_date) 
        return strategy.predict(student_id, course_id, start_date, end_date)
