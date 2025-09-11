from flask import jsonify
from http import HTTPStatus
import time

# Base de datos simulada con 3 productos ficticios
products = [
    {
        'id': '1',
        'name': 'iPhone 15 Pro',
        'description': 'Último smartphone de Apple con chip A17 Pro',
        'price': 999.99,
        'category': 'electronics',
        'tags': ['smartphone', 'apple', 'tecnología'],
        'inStock': True,
        'specifications': {
            'pantalla': '6.1 pulgadas',
            'procesador': 'A17 Pro',
            'almacenamiento': '128GB',
            'cámara': '48MP'
        },
        'ratings': [
            {'score': 5, 'comment': 'Excelente teléfono, muy rápido'},
            {'score': 4, 'comment': 'Buen producto pero caro'}
        ]
    },
    {
        'id': '2',
        'name': 'Libro de Python Avanzado',
        'description': 'Guía completa para programación avanzada en Python',
        'price': 45.50,
        'category': 'books',
        'tags': ['programación', 'python', 'desarrollo'],
        'inStock': True,
        'specifications': {
            'páginas': '350',
            'autor': 'John Doe',
            'editorial': 'Tech Publishing'
        },
        'ratings': [
            {'score': 5, 'comment': 'Muy buen contenido para desarrolladores'}
        ]
    },
    {
        'id': '3',
        'name': 'Zapatillas Deportivas',
        'description': 'Zapatillas cómodas para running y ejercicio',
        'price': 79.99,
        'category': 'ropa',
        'tags': ['deportes', 'running', 'calzado'],
        'inStock': False,
        'specifications': {
            'material': 'Malla transpirable',
            'tallas': '38-45',
            'color': 'Negro/Rojo'
        },
        'ratings': [
            {'score': 4, 'comment': 'Muy cómodas para correr'},
            {'score': 3, 'comment': 'Buenas pero se desgastan rápido'}
        ]
    }
]


def create_product(data):
    """Crear un nuevo producto"""
    # Validar campos requeridos
    required_fields = ['name', 'price', 'category']
    for field in required_fields:
        if field not in data:
            return jsonify({
                'message': 'Campo requerido faltante',
                'details': f'El campo {field} es obligatorio'
            }), HTTPStatus.BAD_REQUEST

    # Crear nuevo producto
    new_product = {
        'id': str(int(time.time() * 1000)),
        'name': data['name'],
        'price': float(data['price']),
        'category': data['category'],
        'description': data.get('description', ''),
        'tags': data.get('tags', []),
        'inStock': data.get('inStock', True),
        'specifications': data.get('specifications', {}),
        'ratings': data.get('ratings', [])
    }

    products.append(new_product)
    return jsonify(new_product), HTTPStatus.CREATED


def get_products(category=None, in_stock=None):
    """Obtener lista de productos con filtros opcionales"""
    filtered_products = products

    # Aplicar filtros
    if category:
        filtered_products = [p for p in filtered_products if p['category'] == category]

    if in_stock is not None:
        in_stock_bool = in_stock.lower() == 'true' if isinstance(in_stock, str) else bool(in_stock)
        filtered_products = [p for p in filtered_products if p['inStock'] == in_stock_bool]

    return jsonify(filtered_products), HTTPStatus.OK


def get_product_by_id(id):
    """Obtener producto por ID"""
    product = next((p for p in products if p['id'] == id), None)

    if product:
        return jsonify(product), HTTPStatus.OK
    else:
        return jsonify({
            'message': 'Producto no encontrado',
            'details': f'No existe un producto con ID {id}'
        }), HTTPStatus.NOT_FOUND


def update_product(id, data):
    """Actualizar producto existente"""
    product = next((p for p in products if p['id'] == id), None)

    if not product:
        return jsonify({
            'message': 'Producto no encontrado',
            'details': f'No existe un producto con ID {id}'
        }), HTTPStatus.NOT_FOUND

    # Actualizar campos permitidos
    updatable_fields = ['name', 'description', 'price', 'category',
                        'tags', 'inStock', 'specifications', 'ratings']

    for field in updatable_fields:
        if field in data:
            product[field] = data[field]

    return jsonify(product), HTTPStatus.OK


def delete_product(id):
    """Eliminar producto"""
    global products
    initial_length = len(products)
    products = [p for p in products if p['id'] != id]

    if len(products) < initial_length:
        return '', HTTPStatus.NO_CONTENT
    else:
        return jsonify({
            'message': 'Producto no encontrado',
            'details': f'No existe un producto con ID {id}'
        }), HTTPStatus.NOT_FOUND