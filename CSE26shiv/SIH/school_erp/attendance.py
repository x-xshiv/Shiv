from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required
from models import db, Student, Attendance
from datetime import date

attendance = Blueprint('attendance', __name__, url_prefix='/attendance')

@attendance.route('/')
@login_required
def attendance_page():
    students = Student.query.all()
    # Get today's date
    today = date.today().isoformat()
    return render_template('attendance.html', students=students, today=today)

@attendance.route('/mark', methods=['POST'])
@login_required
def mark_attendance():
    # Get the attendance data from the form
    attendance_data = request.form.to_dict()
    today = date.today()

    # We expect form data: attendance_1, attendance_2, etc. where the number is student id
    for key, value in attendance_data.items():
        if key.startswith('attendance_'):
            student_id = key.split('_')[1]
            status = value
            # Check if attendance for this student and date already exists
            existing_attendance = Attendance.query.filter_by(student_id=student_id, date=today).first()
            if existing_attendance:
                existing_attendance.status = status
            else:
                new_attendance = Attendance(student_id=student_id, date=today, status=status)
                db.session.add(new_attendance)

    db.session.commit()
    flash('Attendance marked successfully!')
    return redirect(url_for('attendance.attendance_page'))