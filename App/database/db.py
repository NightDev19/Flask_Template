from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):

    __tablename__ = 'users'  # Optional, defaults to 'user'

    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(50), default='user')

    def __init__(self, username: str, password: str, role: str = 'user'):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return f'<User {self.username}>'
