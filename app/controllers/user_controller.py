from flask import jsonify
import time
from http import HTTPStatus

# Simulamos una base de datos en memoria (variable global)
users = [
    {
        'id': '1',
        'name': 'Juan Pérez',
        'age': 25,
        'email': 'juan@ejemplo.com'
    },
    {
        'id': '2',
        'name': 'María García',
        'age': 30,
        'email': 'maria@ejemplo.com'
    },
    {
        'id': '3',
        'name': 'Carlos López',
        'age': 28,
        'email': 'carlos@ejemplo.com'
    },
    {
        'id': '4',
        'name': 'Ana Martínez',
        'age': 22,
        'email': 'ana@ejemplo.com'
    },
    {
        'id': '5',
        'name': 'Pedro Rodríguez',
        'age': 35,
        'email': 'pedro@ejemplo.com'
    },
    {
        'id': '6',
        'name': 'Laura Sánchez',
        'age': 26,
        'email': 'laura@ejemplo.com'
    }
]


def create_user(data):
    """
    Crear un nuevo usuario
    Los datos ya están validados por OpenAPI middleware
    """
    # Desestructuramos los datos del cuerpo de la petición
    name = data['name']
    age = data['age']
    email = data['email']

    # Creamos el nuevo usuario
    new_user = {
        'id': str(int(time.time() * 1000)),  # ID basado en timestamp
        'name': name,
        'age': age,
        'email': email
    }

    # Lo agregamos a nuestra "base de datos"
    users.append(new_user)

    # Enviamos la respuesta con código 201 (Created)
    return jsonify(new_user), HTTPStatus.CREATED


def get_user_by_id(id):
    """
    Obtener usuario por ID
    """
    # Buscamos el usuario en la lista
    user = next((user for user in users if user['id'] == id), None)

    if user:
        return jsonify(user), HTTPStatus.OK
    else:
        return jsonify({
            'message': 'Usuario no encontrado',
            'details': f'No existe un usuario con ID {id}'
        }), HTTPStatus.NOT_FOUND


def update_user(id, data):
    """
    Actualizar usuario existente
    """
    # Buscamos el usuario en la lista
    user = next((user for user in users if user['id'] == id), None)

    if not user:
        return jsonify({
            'message': 'Usuario no encontrado',
            'details': f'No existe un usuario con ID {id}'
        }), HTTPStatus.NOT_FOUND

    # Actualizamos los campos proporcionados
    if 'name' in data:
        user['name'] = data['name']
    if 'age' in data:
        user['age'] = data['age']
    if 'email' in data:
        user['email'] = data['email']

    return jsonify(user), HTTPStatus.OK