from .database.db import db
from sqlalchemy import Column, Integer, String

class User(db.Model):
    __tablename__ = 'users'  # Optional, defaults to 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    role = Column(String(20), default='user')

    def __init__(self, username: str, email: str, password: str, role: str = 'user'):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return f"<User {self.username}>"
