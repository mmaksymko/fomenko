from flask import request, jsonify
from __main__ import app
from service.analytics_facade import AnalyticsFacade

analytics_facade = AnalyticsFacade()

@app.route('/feedback', methods=['GET'])
def feedback():
    feedback = analytics_facade.get_courses_feedback()
    feedback_dict = [f.to_dict() for f in feedback]
    return jsonify(feedback_dict)

@app.route('/attempts-success-ratio', methods=['GET'])
def attempts_success_ratio():
    ratio = analytics_facade.get_attempts_success_ratio()
    ratio_dict = [r.to_dict() for r in ratio]
    return jsonify(ratio_dict)

@app.route('/completion-percentage', methods=['GET'])
def completion_percentage():
    completion_percentage = analytics_facade.calculate_completion_percentage()
    completion_percentage_dict = [c.to_dict() for c in completion_percentage]
    return jsonify(completion_percentage_dict)

@app.route('/score-time-relation', methods=['GET'])
def score_time_correlation():
    cor = analytics_facade.calculate_score_time_correlation()
    cor_dict = [c.to_dict() for c in cor]
    return jsonify(cor_dict)