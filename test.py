from flask import Flask, jsonify, request
from requests import request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/login_test/', methods=['POST'])
def login():
    return "Login endpoint"


@app.route('login/', methods = ['Post'])
def login_user():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "password":
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401