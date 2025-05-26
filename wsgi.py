from flask import Flask
from app.controller.simple_service_controller import simple_service_bp

app = Flask(__name__)
app.register_blueprint(simple_service_bp)

# Health check endpoint
@app.route("/health-check", methods=['GET'])
def health_check():
    return "ok", 200

@app.errorhandler(Exception)
def handle_all_errors(exception):
    return {
        "code": exception.code,
        "name": exception.name,
        "description": exception.description
    }, 500
