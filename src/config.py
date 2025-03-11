import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://padmaja:padmaja@localhost:5432/event_management')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
