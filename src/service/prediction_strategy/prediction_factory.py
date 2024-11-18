from service.prediction_strategy.date_based_prediction_strategy import DateBasedPredictionStrategy
from service.prediction_strategy.course_based_prediction_startegy import CourseBasedPredictionStrategy
from config.singleton import Singleton
  
strategies = {
    "date": DateBasedPredictionStrategy(),
    "course": CourseBasedPredictionStrategy()
}

class PredictionFactory(metaclass=Singleton):
    @staticmethod
    def get_prediction_strategy(course_id=None, start_date=None, end_date=None):
        if start_date and end_date:
            return strategies["date"]
        elif course_id:
            return strategies["course"]
        else:
            raise ValueError("Insufficient parameters for prediction strategy selection.")
