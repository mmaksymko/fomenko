from service.attempt_service import AttemptService
from sqlalchemy import and_
from service.prediction_strategy.prediction_strategy import PredictionStrategy
from model.attempt import Attempt
from model.task import Task
from statsmodels.tsa.holtwinters import ExponentialSmoothing


class DateBasedPredictionStrategy(PredictionStrategy):
    def __init__(self):
        self.attempt_service = AttemptService()
    
    def predict(self, student_id, course_id=None, start_date=None, end_date=None):
        grades = self.attempt_service.get_all_course_attempts_for_student(student_id, course_id) if course_id else self.attempt_service.get_all_attempts_for_student(student_id)
        grades = [g for g in grades if g.date_start > start_date and g.date_finish < end_date] if start_date and end_date else grades
                
        # Return 0 if no grades are available
        if not grades:
            return 0
        
        # Sort grades by date for time-series modeling
        grades.sort(key=lambda g: g.date)
        grade_values = [g.grade for g in grades]
        
        # Apply Exponential Smoothing or EWMA for a smoother trend prediction
        if len(grade_values) > 3:  # Ensure enough data points
            model = ExponentialSmoothing(grade_values, trend="add", seasonal=None, damped_trend=True).fit()
            trend_prediction = model.forecast(steps=1)[0]
        else:
            trend_prediction = sum(grade_values) / len(grade_values)  # Fallback to average if too few points

        # Calculate a simple or exponential weighted moving average as a final metric
        ewma_average = sum(w * g for w, g in enumerate(grade_values, start=1)) / sum(range(1, len(grade_values) + 1))
        
        # Blend trend prediction and EWMA for final output
        final_prediction = 0.6 * trend_prediction + 0.4 * ewma_average
        return final_prediction