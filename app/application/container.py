from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Container:
    flask_app: Flask
    sqlalchemy_db: SQLAlchemy
    client_use_case = None
    client_repository = None

