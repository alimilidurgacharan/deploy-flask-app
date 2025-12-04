from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/login_test/', methods=['POST'])
def login_test():
    return "Login endpoint"


# @app.route('/api/login/', methods=['POST'])
# def login_user():
#     try:
#         data = request.get_json()

#         username = data.get("username")
#         password = data.get("password")

#         return jsonify({
#             "success": True,
#             "username": username
#         })

#     except Exception as e:
#         return jsonify({
#             "success": False,
#             "error": str(e)
#         }), 500

@app.route('/api/login/', methods=['POST'])
def login_user():
    try:
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"success": False, "error": "Username and password are required."}), 400
        return jsonify({"success": True, "username": username}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500