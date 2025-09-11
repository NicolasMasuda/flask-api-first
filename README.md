# APIFirst - API First con Flask y OpenAPI

## Descripción
Este proyecto es un ejemplo de **API First** utilizando **Flask** y **OpenAPI 3.1.1**.  
El objetivo es aprender a definir la API primero mediante un archivo de especificación (`openapi.yaml`) antes de implementar la lógica en Flask, siguiendo buenas prácticas de diseño y documentación.

Se incluye:
- Una estructura modular de Flask (`routes`, `controllers`, `models`).
- Endpoints para `/hello`, `/users` y `/products`.
- Documentación interactiva con **Swagger UI** disponible en `/docs`.
- Exposición del contrato OpenAPI en `/openapi.yaml`.
- **Validación automática de requests** usando OpenAPI Validator.

---

## Conceptos básicos

### API First
API First significa que **primero se define la API** como un contrato (OpenAPI) y luego se implementa. Esto permite:
- Mejor comunicación entre equipos.
- Validación temprana de la API.
- Generación de documentación y clientes automáticamente.

### OpenAPI
OpenAPI es un **estándar para describir APIs REST**. Define:
- Endpoints (`paths`)
- Métodos HTTP (GET, POST, PUT, DELETE)
- Estructura de datos (`schemas`)
- Respuestas esperadas (`responses`)

### Swagger UI
Swagger UI permite **visualizar y probar la API** directamente desde el navegador a partir del archivo OpenAPI.

### OpenAPI Validator
El validador OpenAPI permite **validar automáticamente** las peticiones entrantes contra la especificación definida, similar al middleware.

#### Validación Global (como Express middleware)
- **Una sola configuración** en `app/__init__.py`
- **Validación automática** de todos los requests
- **Sin código repetitivo** en las rutas

#### Rutas Limpias
- **Sin decoradores** en cada función
- **Sin validación manual** en el código
- **Enfoque en la lógica de negocio**

#### Consistencia con OpenAPI
- **Validación directa** desde el archivo `openapi.yaml`
- **Sincronización automática** entre documentación y validación
- **API First** real: el contrato define el comportamiento

#### Conclusión

La implementación de OpenAPI Validator en Flask proporciona:

✅ **Validación automática** de requests contra la especificación OpenAPI  
✅ **Rutas limpias** sin código de validación repetitivo  
✅ **Middleware global** similar a Express.js  
✅ **Manejo consistente** de errores de validación  
✅ **API First** verdadero donde el contrato define el comportamiento  

Este enfoque optimiza el desarrollo al garantizar que todas las peticiones cumplan con la especificación OpenAPI definida, facilitando el mantenimiento y la comunicación entre equipos.

---

## Herramientas de Desarrollo y Testing

### Postman
**Postman** es una herramienta esencial para el desarrollo y testing de APIs. Permite:
- Crear y organizar collections de endpoints
- Realizar pruebas manuales e interactivas
- Configurar environments para diferentes entornos
- Automatizar pruebas con scripts
- Documentar APIs de manera colaborativa

### Newman
**Newman** es el CLI (Command Line Interface) de Postman que permite:
- Ejecutar collections de Postman desde la terminal
- Integrar testing de APIs en pipelines CI/CD
- Generar reportes en múltiples formatos (HTML, JSON, etc.)
- Automatizar pruebas de regresión
- Ejecutar pruebas en entornos headless

### Swagger Editor
**Swagger Editor** (disponible en https://editor.swagger.io/) es una herramienta online que permite:
- Editar archivos OpenAPI/YAML con sintaxis highlight
- Validar la especificación OpenAPI en tiempo real
- Visualizar la documentación automáticamente
- Generar código cliente y servidor
- Colaborar en el diseño de APIs

---

## Estructura del proyecto

```text
APIFirst/
│── app.py
│── requirements.txt
│── openapi.yaml                    ← Especificación completa OpenAPI
│
├── app/
│   ├── __init__.py                 ← Validador global
│   ├── routes/
│   │    ├── hello.py               ← Endpoint hello
│   │    ├── auth.py                ← Endpoint auth
│   │    ├── users.py               ← Endpoints de usuarios
│   │    ├── products.py            ← Endpoints de productos
│   │    └── docs.py                ← Documentación Swagger
│   └── controllers/
│        ├── auth_controller.py
│        ├── hello_controller.py
│        ├── user_controller.py     ← Lógica de usuarios
│        └── products_controller.py ← Lógica de productos
```

---

## Instalación y uso

```bash
# Clonar el proyecto
git clone <url-del-repositorio>
cd APIFirst

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python app.py
```

La aplicación estará disponible en `http://127.0.0.1:5000`

---

## Endpoints disponibles

- `GET /hello` - Endpoint de prueba
- `POST /users` - Crear usuario
- `GET /users/{id}` - Obtener usuario por ID
- `POST /users/{id}` - Actualizar usuario
- `POST /products` - Crear producto
- `GET /products` - Listar productos
- `GET /products/{id}` - Obtener producto por ID
- `PUT /products/{id}` - Actualizar producto
- `DELETE /products/{id}` - Eliminar producto
- `GET /docs` - Documentación Swagger UI
- `GET /openapi.yaml` - Especificación OpenAPI

---

## Flujo de trabajo recomendado

1. **Diseñar** la API en `openapi.yaml` usando Swagger Editor
2. **Validar** el diseño con https://editor.swagger.io/
3. **Implementar** los endpoints en Flask
4. **Probar** manualmente con Postman
5. **Automatizar** pruebas con Newman
6. **Iterar** y mejorar el diseño basado en feedback

---

## Próximos pasos

- [ ] Agregar autenticación JWT
- [ ] Implementar base de datos real
- [ ] Agregar más validaciones personalizadas
- [ ] Crear tests unitarios
- [ ] Configurar CI/CD con Newman
- [ ] Dockerizar la aplicación

Este enfoque de **API First** asegura que tu API esté bien diseñada, documentada y lista para ser consumida por clientes frontend y móviles desde el primer día.