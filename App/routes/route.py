from flask import render_template, url_for, redirect, request, flash
from flask_login import login_user, logout_user
from App.auth.auth_controller import AuthController
from App.auth.middleware import require_role
from App.database.db import db, User


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

        # Login Route
        @self.app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']
                if AuthController.login(username, password):
                    flash("Login successful!", "success")
                    return redirect(url_for("user_dashboard"))
                flash("Invalid credentials. Please try again.", "error")
            return render_template("Views/login.html")

        # Signup Route
        @self.app.route('/signup', methods=['GET', 'POST'])
        def signup():
            if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']
                if AuthController.signup(username, password):
                    flash("Signup successful. You can now log in.", "success")
                    return redirect(url_for("login"))
                flash("Username already exists. Please try again.", "error")
            return render_template("Views/signup.html")

        # Dashboard Route (requires authentication and role check)
        @self.app.route('/dashboard')
        @require_role("user")  # Use middleware to restrict role-based access
        def user_dashboard():
            user = AuthController.current_user()
            return render_template("Views/dashboard.html", user=user)

        # Admin Dashboard Route
        @self.app.route('/admin-dashboard')
        @require_role("admin")
        def admin_dashboard():
            return render_template("Views/admin_dashboard.html")

        # Logout Route
        @self.app.route('/logout')
        def logout():
            AuthController.logout()
            flash("You have been logged out.", "info")
            return redirect(url_for("home"))
