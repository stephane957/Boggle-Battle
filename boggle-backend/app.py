from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
cors = CORS()

def create_app(config_class=Config):
    app = Flask('boggle-battle')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlalchemy_testdb.db'

    db.init_app(app)
    cors.init_app(app)

    with app.app_context():
        from routes import init_routes
        init_routes(app)
        db.create_all()  # Create tables

    migrate = Migrate(app, db)

    return app