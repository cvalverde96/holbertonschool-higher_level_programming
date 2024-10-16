#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route("/")
def home():
    return ("Welcome to the Flask API!")


@app.route("/data")
def getting_usernames():
    return (jsonify(list(users.keys())))


@app.route("/status")
def status_code():
    return ("OK")


@app.route("/users/<username>")
def full_object(username):
    user = users.get(username)
    if user:
        return (jsonify(user))
    else:
        return (jsonify({"error": "User not found"}), 404)


@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json()
    
    if "username" not in new_user:
        return (jsonify({"error": "Username is required"}), 400)
    
    username = new_user("username")
    
    users[username] = new_user
    
    return (jsonify({
        "message": "User added",
        "user": new_user
    }), 201)


if __name__ == "__main__":
    app.run(debug=True)
