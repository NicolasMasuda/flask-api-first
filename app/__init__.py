import os
from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

# openapi-core imports
from openapi_core import OpenAPI
from openapi_core.validation.request.validators import V30RequestValidator
from openapi_core.contrib.flask import FlaskOpenAPIRequest


def create_app():
    app = Flask(__name__)

    # === 1. Cargar OpenAPI Spec ===
    base_dir = os.path.abspath(os.path.dirname(__file__))
    root_dir = os.path.dirname(base_dir)
    spec_path = os.path.join(root_dir, "openapi.yaml")

    try:
        openapi = OpenAPI.from_file_path(spec_path)
        # CORRECCIÓN: Usar openapi.spec en lugar de openapi
        request_validator = V30RequestValidator(openapi.spec)
        print("✅ OpenAPI validator loaded successfully")
    except Exception as e:
        print(f"❌ Error loading validator: {e}")
        request_validator = None

    # === 2. Validar REQUEST solo para rutas definidas en OpenAPI ===
    @app.before_request
    def validate_request():
        skip_paths = [
            "/docs", "/openapi.yaml", "/openapi.json",
            "/static", "/favicon.ico", "/apple-touch-icon",
            "/__debugger__"
        ]

        if any(request.path.startswith(path) for path in skip_paths):
            return

        if request.path == "/":
            return

        if request.method == "OPTIONS":
            return

        if not request_validator:
            return

        # Solo validar rutas que están en tu spec
        api_paths = ["/hello", "/users"]
        if not any(request.path.startswith(path) for path in api_paths):
            return

        try:
            openapi_request = FlaskOpenAPIRequest(request)
            result = request_validator.validate(openapi_request)

            # CORRECCIÓN: Verificar que result no sea None antes de acceder a .errors
            if result is not None and hasattr(result, 'errors') and result.errors:
                error = result.errors[0]
                return jsonify({
                    "message": "Request validation error",
                    "details": str(error),
                }), 400

        except Exception as e:
            # Log simple y limpio - sin traceback completo
            error_type = type(e).__name__
            print(f"API Validation Error ({error_type}): {str(e)}")

            # Extraer mensajes de error más específicos si están disponibles
            error_message = str(e)
            if hasattr(e, '__cause__') and hasattr(e.__cause__, 'schema_errors'):
                # Para errores de schema, obtener los mensajes específicos
                schema_errors = []
                for schema_error in e.__cause__.schema_errors:
                    schema_errors.append(str(schema_error))
                if schema_errors:
                    error_message = "; ".join(schema_errors)

            return jsonify({
                "message": "Invalid request data",
                "details": error_message,
            }), 400

    # === 3. Swagger UI ===
    SWAGGER_URL = "/docs"
    API_URL = "/openapi.yaml"
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={"app_name": "APIFirst"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # === 4. Registrar rutas ===
    from app.routes.hello import hello_bp
    from app.routes.docs import docs_bp
    from app.routes.users import users_bp
    from app.routes.products import products_bp

    app.register_blueprint(hello_bp)
    app.register_blueprint(docs_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(products_bp)

    # === 5. Ruta de inicio simple ===
    @app.route('/')
    def index():
        return jsonify({
            'message': 'API First Flask Server',
            'docs': '/docs',
            'spec': '/openapi.yaml'
        })

    # === 6. Manejador de errores ===
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'message': 'Endpoint not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'message': 'Internal server error',
            'details': str(error)
        }), 500

    return app