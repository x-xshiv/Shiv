from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models import db, Student, User
from datetime import date

student = Blueprint('student', __name__, url_prefix='/student')

@student.route('/')
@login_required
def student_list():
    students = Student.query.all()
    return render_template('student_list.html', students=students)

@student.route('/add', methods=['GET', 'POST'])
@login_required
def add_student():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        dob = request.form.get('dob')
        grade = request.form.get('grade')
        parent_id = request.form.get('parent_id')

        # Convert string to date
        dob = date.fromisoformat(dob)

        new_student = Student(first_name=first_name, last_name=last_name, date_of_birth=dob, grade=grade, parent_id=parent_id)
        db.session.add(new_student)
        db.session.commit()
        flash('Student added successfully!')
        return redirect(url_for('student.student_list'))

    # Get list of parents (users with role 'parent')
    parents = User.query.filter_by(role='parent').all()
    return render_template('student_form.html', parents=parents)

@student.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_student(id):
    student = Student.query.get_or_404(id)
    if request.method == 'POST':
        student.first_name = request.form.get('first_name')
        student.last_name = request.form.get('last_name')
        student.date_of_birth = date.fromisoformat(request.form.get('dob'))
        student.grade = request.form.get('grade')
        student.parent_id = request.form.get('parent_id')
        db.session.commit()
        flash('Student updated successfully!')
        return redirect(url_for('student.student_list'))

    parents = User.query.filter_by(role='parent').all()
    return render_template('student_form.html', student=student, parents=parents)

@student.route('/delete/<int:id>')
@login_required
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted successfully!')
    return redirect(url_for('student.student_list'))