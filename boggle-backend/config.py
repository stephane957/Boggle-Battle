import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', "sqlite:///sqlalchemy_example.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False