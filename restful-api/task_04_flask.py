#!/usr/bin/python3

"""
part 1
Setting Up Flask
"""
# importando Flask
from flask import Flask
from flask import jsonify
from flask import request

# instantiating un servidor web de Flask
app = Flask(__name__)

"""
part 2
Creating Your First Endpoint
"""


@app.route("/")
def home():
    return ("Welcome to the Flask API!")


if __name__ == "__main__":
    app.run()

"""
part 3
Serving JSON Data
"""


users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/data")
def usernames():
    return (jsonify(users))


"""
part 4
Expanding Your API
"""


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


"""
part 5
Handling POST Requests
"""


@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json()

    username = new_user.get("username")

    if username in users:
        return (jsonify({"error": "User already exists"}), 400)

    users[username] = {
        "name": new_user.get("name"),
        "age": new_user.get("age"),
        "city": new_user.get("city")
    }

    return (jsonify({"message": "User added", "user": users[username]}))
