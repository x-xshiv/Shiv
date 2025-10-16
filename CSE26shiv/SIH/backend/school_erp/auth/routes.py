from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token
from models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    if user and user.password == password:  # Use hashed passwords in production!
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token, role=user.role), 200
    
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route('/profile')
@jwt_required()
def profile():
    # Access current user with get_jwt_identity()
    return jsonify({"message": "Protected profile"})