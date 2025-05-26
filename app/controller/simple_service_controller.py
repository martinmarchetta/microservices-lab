from flask import Blueprint, jsonify
from flask import request

simple_service_bp = Blueprint('simple_service', __name__, url_prefix='/simple-service')

# Misc controller endpoints
@simple_service_bp.route("/mensaje/<mensaje>", methods=['POST'])
def retornar_mensaje(mensaje: str):
    return jsonify({
        "status": "ok",
        "mensaje": f"Me llego este mensaje: '{mensaje}'"
    }), 200

@simple_service_bp.route("/headers", methods=['GET'])
def retornar_headers_get():
    return jsonify(dict(request.headers)), 200

@simple_service_bp.route("/headers", methods=['POST'])
def retornar_headers_post():
    headers = request.headers
    payload = None
    http_response_code = 0
    if headers['Accept'] == 'application/json':
        payload = jsonify({
            'status': 'ok',
            'data': [
                {
                'id': 1,
                'description': 'Primer dato'
                },
                {
                'id': 2,
                'description': 'Segundo dato'
                },
                {
                'id': 3,
                'description': 'Tercer dato'
                }
            ]
        })
        http_response_code = 200
    else:
        payload = f"Return content type {headers['Accept']} is not supported"
        http_response_code = 406

    return payload, http_response_code
