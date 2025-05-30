from flask import Blueprint, jsonify, request
from app.use_case.client_use_case import ClientUseCase

client_bp = Blueprint('client', __name__, url_prefix='/client')

def initialize_client_routes():
    """
    Initialize client routes with the given database session
    """
    client_use_case = ClientUseCase()

    @client_bp.route('/', methods=['GET'])
    def get_all_clients():
        """Get all clients"""
        clients = client_use_case.get_all_clients()
        return jsonify([{
            'id': client.id,
            'name': client.client_name,
            'address': client.client_address
        } for client in clients]), 200

    @client_bp.route('/<int:client_id>', methods=['GET'])
    def get_client(client_id: int):
        """Get a specific client by ID"""
        client = client_use_case.get_client_by_id(client_id)
        if not client:
            return jsonify({'error': 'Client not found'}), 404
        return jsonify({
            'id': client.id,
            'name': client.client_name,
            'address': client.client_address
        }), 200

    @client_bp.route('/', methods=['POST'])
    def create_client():
        """Create a new client"""
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({'error': 'Client name is required'}), 400

        client = client_use_case.create_client(
            client_name=data['name'],
            client_address=data.get('address', '')
        )
        return jsonify({
            'id': client.id,
            'name': client.client_name,
            'address': client.client_address
        }), 201

    @client_bp.route('/<int:client_id>', methods=['PUT'])
    def update_client(client_id: int):
        """Update an existing client"""
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        update_data = {}
        if 'name' in data:
            update_data['client_name'] = data['name']
        if 'address' in data:
            update_data['client_address'] = data['address']

        client = client_use_case.update_client(client_id, update_data)
        if not client:
            return jsonify({'error': 'Client not found'}), 404

        return jsonify({
            'id': client.id,
            'name': client.client_name,
            'address': client.client_address
        }), 200

    @client_bp.route('/<int:client_id>', methods=['DELETE'])
    def delete_client(client_id: int):
        """Delete a client"""
        success = client_use_case.delete_client(client_id)
        if not success:
            return jsonify({'error': 'Client not found'}), 404
        return jsonify({'message': 'Client deleted successfully'}), 200

    return client_bp
