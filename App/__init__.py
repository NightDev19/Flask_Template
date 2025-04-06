from flask import Flask
from .config import Config
from .database.db import db

class App:
    def __init__(self,name):
        self.name = name
        self.app = Flask(name)

        # FixMe : Connect to the database in Schema (Done)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATA_URI
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['SECRET_KEY'] = Config.SECRET_KEY



    def create_app(self):
        # self.app.config.from_object('config.Config')
        # self.app.config.from_envvar('FLASK_CONFIG', silent=True)

        # Register blueprints here
        from App.routes.route import MainRoute, UserRoute
        MainRoute(self.app)
        UserRoute(self.app)

        db.init_app(self.app)

        return self.app
