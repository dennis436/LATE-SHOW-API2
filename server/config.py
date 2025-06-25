import os

DATABASE_URI = "postgresql://late_user:late_pass@localhost:5432/late_show_db"


class Config:
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your-secret-key'  # Change this in production!
