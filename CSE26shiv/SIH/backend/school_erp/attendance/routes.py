from flask import Blueprint, request, jsonify
from models import db, Attendance, Student

attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/mark', methods=['POST'])
def mark_attendance():
    data = request.json
    new_record = Attendance(
        student_id=data['student_id'],
        date=data['date'],
        status=data['status']
    )
    db.session.add(new_record)
    db.session.commit()
    return jsonify({"message": "Attendance marked"}), 201

@attendance_bp.route('/report/<int:student_id>')
def attendance_report(student_id):
    records = Attendance.query.filter_by(student_id=student_id).all()
    return jsonify([{
        'date': r.date.isoformat(),
        'status': r.status
    } for r in records])