from flask import Flask, jsonify, request
from requests import request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/login_test/', methods=['POST'])
def login_test():
    return "Login endpoint"


@app.route('/login/', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    # Very basic authentication (for example only)
    if username == "admin" and password == "123456":
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401