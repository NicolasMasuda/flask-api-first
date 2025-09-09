import os
import yaml
from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

# openapi-core imports (solo request validator)
from openapi_core import OpenAPI
from openapi_core.validation.request.validators import V30RequestValidator
from openapi_core.contrib.flask import FlaskOpenAPIRequest


def create_app():
    app = Flask(__name__)

    # === 1. Cargar OpenAPI Spec ===
    base_dir = os.path.abspath(os.path.dirname(__file__))  # app/
    root_dir = os.path.dirname(base_dir)  # APIFirst/
    spec_path = os.path.join(root_dir, "openapi.yaml")

    with open(spec_path, "r") as f:
        spec_dict = yaml.safe_load(f)

    # Usar OpenAPI
    spec = OpenAPI.from_dict(spec_dict)

    # Crear solo validador de request
    request_validator = V30RequestValidator(spec)

    # === 2. Validar REQUEST antes de las rutas ===
    @app.before_request
    def validate_request():
        # Ignorar docs y archivos estáticos
        if request.path.startswith("/docs") or request.path == "/openapi.yaml":
            return

        try:
            openapi_request = FlaskOpenAPIRequest(request)
            result = request_validator.validate(openapi_request)

            if result.errors:
                error = result.errors[0]
                return jsonify({
                    "message": "Request validation error",
                    "details": str(error),
                }), 400
        except Exception as e:
            # Si hay error en la validación, loguear pero no fallar
            print(f"Validation error: {e}")
            return

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
    app.register_blueprint(hello_bp)
    app.register_blueprint(docs_bp)

    # === 5. Manejador global de errores ===
    @app.errorhandler(Exception)
    def handle_error(error):
        return jsonify({
            "message": "Internal server error",
            "details": str(error),
        }), 500

    return app