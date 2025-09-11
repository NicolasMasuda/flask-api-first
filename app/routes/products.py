from flask import Blueprint, request
from app.controllers.products_controller import (
    create_product,
    get_products,
    get_product_by_id,
    update_product,
    delete_product
)

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['POST'])
def create_product_route():
    """Crear un nuevo producto"""
    return create_product(request.get_json())

@products_bp.route('/products', methods=['GET'])
def get_products_route():
    """Obtener lista de productos"""
    category = request.args.get('category')
    in_stock = request.args.get('inStock')
    return get_products(category, in_stock)

@products_bp.route('/products/<string:id>', methods=['GET'])
def get_product_route(id):
    """Obtener un producto por ID"""
    return get_product_by_id(id)

@products_bp.route('/products/<string:id>', methods=['PUT'])
def update_product_route(id):
    """Actualizar un producto existente"""
    return update_product(id, request.get_json())

@products_bp.route('/products/<string:id>', methods=['DELETE'])
def delete_product_route(id):
    """Eliminar un producto"""
    return delete_product(id)