from flask import request, jsonify
from __main__ import app
from service.analytics_facade import AnalyticsFacade

analytics_facade = AnalyticsFacade()

@app.route('/users', methods=['GET'])
def filter_users_route():
    course_id = request.args.get('course_id', type=int)
    grade = request.args.get('grade', type=float)
    group_number = request.args.get('group_number', type=int)
    entry_year = request.args.get('entry_year', type=int)
    speciality_shortened = request.args.get('speciality_shortened', type=str)
    sort_by = request.args.get('sort_by', type=str, default=None)
    order = request.args.get('order', type=str, default='asc')
    
    users = analytics_facade.get_users(course_id, grade, group_number, entry_year, speciality_shortened, sort_by, order)
    
    users_dict = [user.to_dict() for user in users]
    
    return jsonify(users_dict)