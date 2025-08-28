import os
from flask import Flask, send_file
from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    app = Flask(__name__)

    # Ruta para servir el openapi.yaml desde la raíz del proyecto
    @app.route("/openapi.yaml")
    def openapi_spec():
        base_dir = os.path.abspath(os.path.dirname(__file__))  # app/
        root_dir = os.path.dirname(base_dir)                   # APIFirst/
        return send_file(os.path.join(root_dir, "openapi.yaml"))

    # Swagger UI
    SWAGGER_URL = "/docs"
    API_URL = "/openapi.yaml"
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={"app_name": "AppFirst"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # Registrar rutas
    from app.routes.hello import hello_bp
    app.register_blueprint(hello_bp)

    return app