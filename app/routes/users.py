from flask import Blueprint, request
from app.controllers.user_controller import create_user

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['POST'])
def create_user_route():  # Cambia el nombre aquí
    """
    Crear usuario - La validación ya se hizo automáticamente
    No necesitamos validar los datos, OpenAPI ya lo hizo por nosotros
    """
    return create_user(request.get_json())