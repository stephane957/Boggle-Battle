import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'boggle-battle-secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///boggle.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = 'Content-Type'
