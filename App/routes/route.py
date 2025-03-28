from flask import render_template,url_for
# Todo: Add more routes and views as needed
class MainRoute:
    def __init__(self, app):
        self.app = app
        self.register_routes()

    def register_routes(self):
        @self.app.route('/')
        def home():
            return render_template('Views/main.html')

        @self.app.route('/about')
        def about():
            return "This is the About Page!"

class UserRoute:
    def __init__(self, app):
        self.app = app
        self.register_routes()

    def register_routes(self):
        @self.app.route('/user/<username>')
        def user_profile(username):
            return f"User Profile: {username}"
