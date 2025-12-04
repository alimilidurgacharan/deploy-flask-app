# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from flask_mail import Mail, Message
# import re
# import os

# app = Flask(__name__)
# CORS(app)

# # Email configuration
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_HOST_USER')  # Your email
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_HOST_PASSWORD')  # Your email password
# app.config['RECIPIENT_EMAIL'] = os.environ.get('RECIPIENT_EMAIL')  # Recipient email

# mail = Mail(app)

# @app.route('/api/check/', methods=['GET'])
# def health_check():
#     return jsonify("hello world"), 200

# @app.route('/api/send-contact-details/', methods=['POST'])
# def send_contact_details():
#     try:
#         data = request.get_json()
        
#         name = data.get("name")
#         email = data.get("email")
#         number = data.get("number")

#         if not all([name, email, number]):
#             return jsonify({"error": "All fields are required."}), 400
        
#         email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#         if not re.match(email_regex, email):    
#             return jsonify({"error": "Invalid email format."}), 400
        
#         subject = "New Contact Form Submission"
#         message_body = f"""
#         Name: {name}
#         Email: {email}
#         Number: {number}
#         """

#         msg = Message(
#             subject=subject,
#             sender=app.config['MAIL_USERNAME'],
#             recipients=[app.config['RECIPIENT_EMAIL']],
#             body=message_body
#         )
        
#         mail.send(msg)
        
#         return jsonify({"message": "Contact details sent successfully."}), 200
    
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000, debug=True)/

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

