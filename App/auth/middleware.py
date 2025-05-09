from functools import wraps
from flask import redirect, url_for, flash
from App.auth.auth_controller import AuthController

def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not AuthController.is_authenticated():
                flash("❌ Access denied. Please log in.", "error")
                return redirect(url_for("login"))  # Or any login route name
            user = AuthController.current_user()
            if user["role"] != role:
                flash(f"❌ Access denied. You must be a {role}.", "error")
                return redirect(url_for("unauthorized"))  # Define this route if needed
            return func(*args, **kwargs)
        return wrapper
    return decorator
