from flask import request, jsonify
from __main__ import app
from service.analytics_facade import AnalyticsFacade

analytics_facade = AnalyticsFacade()

@app.route('/grades/average', methods=['GET'])
def get_average_grade():
    student_id = request.args.get('student_id', type=int)
    course_id = request.args.get('course_id', type=int)
    
    if student_id is None or course_id is None:
        result = analytics_facade.get_average_grades_for_all_users()
        return result
    
    average_grade = analytics_facade.get_average_grade(student_id, course_id)
    return jsonify({"average_grade": average_grade})

@app.route('/grades/total', methods=['GET'])
def get_total_score():
    student_id = request.args.get('student_id', type=int)
    course_id = request.args.get('course_id', type=int)
    
    if student_id is None or course_id is None:
        result = analytics_facade.get_total_scores_for_all_users()
        return result
    
    total_score = analytics_facade.get_total_score(student_id, course_id)
    return jsonify({"total_score": total_score})

@app.route('/grades/predict', methods=['GET'])
def predict_grade():
    student_id = request.args.get('student_id', type=int)
    course_id = request.args.get('course_id', type=int, default=None)
    start_date = request.args.get('start_date', type=str, default=None)
    end_date = request.args.get('end_date', type=str, default=None)
    strategy = request.args.get('strategy', type=int) or 'course'

    if student_id is None:
        return jsonify({"error": "student_id is required"}), 400

    predicted_grade = analytics_facade.predict_grade(student_id, course_id, strategy, start_date, end_date)
    return jsonify({"predicted_grade": predicted_grade})