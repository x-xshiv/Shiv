from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_erp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db
db.init_app(app)

from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from student_management import student as student_blueprint
app.register_blueprint(student_blueprint)

from attendance import attendance as attendance_blueprint
app.register_blueprint(attendance_blueprint)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

def get_user_role():
    # Helper function to get current user's role
    if current_user.is_authenticated:
        return current_user.role
    return None

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
@login_required
def dashboard():
    role = get_user_role()
    return render_template('dashboard.html', role=role)

if __name__ == '__main__':
    app.run(debug=True)