from flask import Flask
from app.controller.simple_service_controller import simple_service_bp
from app.controller.client_controller import client_bp, initialize_client_routes
from yoyo_main import run_migrations
from flask_sqlalchemy import SQLAlchemy
from app.application.config import Config
from app.application.container import Container

# Run migrations (i.e. update the database structure)
run_migrations()

# Create flask app
app = Flask(__name__)
Container.flask_app = app
app.config.from_object(Config)
Container.sqlalchemy_db = SQLAlchemy(app)

# Register blueprints ("planos" de la app). These contain the endpoint declarations and controller methdos and classes
# Simple Service blueprint
app.register_blueprint(simple_service_bp)

# Client blueprint
client_blueprint = initialize_client_routes()
app.register_blueprint(client_blueprint)
