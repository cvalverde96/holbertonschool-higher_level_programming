#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def ver_pass(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return (username)


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return (jsonify(message="Basic Auth: Access Granted"))


if __name__ == "__main__":
    app.run(debug=True)


app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(users[username]["password"], password):
        access_token = create_access_token(identity={"username": username, "role": users[username]["role"]})
        return (jsonify(access_token=access_token), 200)
    return (jsonify({"msg": "Bad credentials"}), 401)


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return (jsonify(message=f"JWT Auth: Access Granted for {current_user['username']}"))


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return (jsonify({"error": "Admin access required"}), 403)
    return (jsonify(message="Admin Access: Granted"))


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return (jsonify({"error": "Missing or invalid token"}), 401)


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return (jsonify({"error": "Invalid token"}), 401)


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return (jsonify({"error": "Token has expired"}), 401)


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return (jsonify({"error": "Token has been revoked"}), 401)


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return (jsonify({"error": "Fresh token required"}), 401)
