from flask import Blueprint, request, jsonify
from models import db, Student

students_bp = Blueprint('students', __name__)

@students_bp.route('/', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{
        'id': s.id,
        'name': f"{s.first_name} {s.last_name}",
        'grade': s.grade
    } for s in students])

@students_bp.route('/', methods=['POST'])
def create_student():
    data = request.json
    new_student = Student(
        username=data['username'],
        password=data['password'],  # Hash in production!
        first_name=data['first_name'],
        last_name=data['last_name'],
        dob=data['dob'],
        grade=data['grade']
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student created"}), 201