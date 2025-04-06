from App import App
from App.database.db import db
from App.models import User


if __name__ == '__main__':
    App = App('App')
    app = App.create_app()

    with app.app_context():
        db.drop_all()
        db.create_all()

        new_user = User(username='testuser', email='test@example.com', password='secret')

        db.session.add(new_user)
        
        db.session.commit()
    app.run(debug=True)
