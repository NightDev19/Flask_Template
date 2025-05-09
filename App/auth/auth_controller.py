from werkzeug.security import generate_password_hash, check_password_hash
from flask import session
from App.database.db import db, User

class AuthController:

    @staticmethod
    def login(username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user'] = {
                "id": user.id,
                "username": user.username,
                "role": user.role
            }
            return True
        return False

    @staticmethod
    def logout():
        session.pop('user', None)

    @staticmethod
    def is_authenticated():
        return 'user' in session

    @staticmethod
    def current_user():
        return session.get('user') if 'user' in session else None

    @staticmethod
    def signup(username, password):
        if User.query.filter_by(username=username).first():
            return False  # Username already exists

        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        return True
