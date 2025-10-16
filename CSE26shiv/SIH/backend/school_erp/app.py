from flask import Flask, jsonify
from flask_migrate import Migrate
from config import Config
from models import db, User, Student, Attendance

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

# Register Blueprints
from auth.routes import auth_bp
from students.routes import students_bp
from attendance.routes import attendance_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(students_bp, url_prefix='/students')
app.register_blueprint(attendance_bp, url_prefix='/attendance')

@app.route('/')
def index():
    return jsonify({"message": "School ERP API"})

if __name__ == '__main__':
    app.run(debug=True)