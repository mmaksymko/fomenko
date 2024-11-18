import os
from flask import Flask
from sqlalchemy import text
from model import db
from config.database_session_manager import DatabaseSessionManager
from model.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

# Import your controllers and models
import controller.grade_controller
import controller.user_controller
import controller.task_analysis_controller

# Initialize the database
db.init_app(app)
session_manager = DatabaseSessionManager()

# Function to check if the database has records
def is_database_empty():
    # Adjust 'User' to a primary model in your application that will have records.
    return db.session.query(User).first() is None

# Function to load SQL file
def load_sql_script(filename):
    with open(filename, 'r') as file:
        sql_script = file.read()
    
    # Split the script into individual statements
    statements = sql_script.split(';')
    
    for statement in statements:
        if statement.strip():
            db.session.execute(text(statement.strip()))
    
    db.session.commit()

# Main application entry point
if __name__ == '__main__':
    with app.app_context():
        # Create all tables
        db.create_all()

        # Load initial data if the database is empty
        if is_database_empty():
            print("Database is empty, loading initial data...")
            load_sql_script('sql/populate.sql')
        else:
            print("Database already populated.")

    # Run the application
    app.run(debug=True)
