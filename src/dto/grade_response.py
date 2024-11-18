class GradeResponse:
    def __init__(self, user_id, first_name, last_name, grades):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'grades': self.grades
        }
