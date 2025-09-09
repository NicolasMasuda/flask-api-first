import os
from flask import Blueprint, send_file

docs_bp = Blueprint("docs", __name__)

@docs_bp.route("/openapi.yaml")
def openapi_spec():
    """
    Servir el archivo OpenAPI YAML desde la raíz del proyecto.
    """
    base_dir = os.path.abspath(os.path.dirname(__file__))  # app/routes
    root_dir = os.path.dirname(os.path.dirname(base_dir))  # APIFirst
    return send_file(os.path.join(root_dir, "openapi.yaml"))