from flask import jsonify
import time

# Simulamos una base de datos en memoria (variable global)
users = []

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
    return jsonify(new_user), 201