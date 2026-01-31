from flask import Blueprint, jsonify

# Define a Blueprint for user routes
user_routes_bp = Blueprint("user_routes", __name__)

# Route to register a new user
@user_routes_bp.route("/user", methods=["POST"])
def registry_user():
    return jsonify({"route": "User registration route"}), 200
