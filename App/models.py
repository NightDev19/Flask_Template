
class User:
    def __init__(self, username: str, email: str, password: str, role: str = 'user'):
        self.username = username
        self.email = email

    def __repr__(self):
        return f"<User {self.username}>"
