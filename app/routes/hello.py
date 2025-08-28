from flask import Blueprint, jsonify
from app.controllers.hello_controller import get_hello

hello_bp = Blueprint("hello", __name__)

@hello_bp.route("/hello", methods=["GET"])
def hello_route():
    return jsonify(get_hello())