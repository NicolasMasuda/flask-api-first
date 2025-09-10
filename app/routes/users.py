from flask import Blueprint, request, jsonify
from app.controllers.user_controller import create_user, get_user_by_id, update_user

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['POST'])
def create_user_route():
    """
    Crear usuario - La validación ya se hizo automáticamente
    No necesitamos validar los datos, OpenAPI ya lo hizo por nosotros
    """
    return create_user(request.get_json())

@users_bp.route('/users/<string:id>', methods=['GET'])
def get_user_route(id):
    """
    Obtener usuario por ID
    """
    return get_user_by_id(id)

@users_bp.route('/users/<string:id>', methods=['POST'])
def update_user_route(id):
    """
    Actualizar usuario existente
    Los datos ya están validados por OpenAPI middleware
    """
    return update_user(id, request.get_json())