# Make an auth module
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

class Auth:
    def __init__(self, db):
        self.db = db
        self.auth_bp = Blueprint('auth', __name__)

        @self.auth_bp.route('/register', methods=['POST'])
        def register():
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                return jsonify({'message': 'Username and password are required!'}), 400

            hashed_password = generate_password_hash(password, method='sha256')
            new_user = {'username': username, 'password': hashed_password}
            self.db.users.insert_one(new_user)

            return jsonify({'message': 'User registered successfully!'}), 201

        @self.auth_bp.route('/login', methods=['POST'])
        def login():
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')

            user = self.db.users.find_one({'username': username})
            if not user or not check_password_hash(user['password'], password):
                return jsonify({'message': 'Invalid credentials!'}), 401

            access_token = create_access_token(identity=username)
            return jsonify({'access_token': access_token}), 200

        @self.auth_bp.route('/protected', methods=['GET'])
        @jwt_required()
        def protected():
            current_user = get_jwt_identity()
            return jsonify({'message': f'Welcome {current_user}!'}), 200
