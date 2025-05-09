from App.database.db import db
from App import App as AppModule  # Rename the imported module to avoid collision
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


if __name__ == '__main__':
    app_instance = AppModule('App')  # Use a different name
    app = app_instance.create_app()

    with app.app_context():
        db.drop_all()
        db.create_all()

    app.run(debug=True)
