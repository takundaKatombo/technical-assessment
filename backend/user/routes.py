from flask import Flask, request, jsonify, Blueprint
from firebase_admin import firestore, credentials, initialize_app
import os
from firebase_admin import messaging
from flask_cors import CORS, cross_origin


current_dir = os.path.dirname(os.path.abspath(__file__))
cred_path = os.path.join(current_dir, '..', 'keys', 'technical-assessment-d3ea8-firebase-adminsdk-elk7v-5650612bf7.json')
cred = credentials.Certificate(cred_path)

# Initialize Flask app and Firebase Admin SDK
app = Flask(__name__)
# cred = credentials.Certificate('backend/keys/technical-assessment-d3ea8-firebase-adminsdk-elk7v-5650612bf7.json')
initialize_app(cred)
db = firestore.client()

# Define the admin blueprint
user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/register', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def register_user():
    try:
        data = request.get_json()
        # Add a new user to Firestore
        user_ref = db.collection('users').document()
        user_ref.set(data)
        
        response = jsonify({"id": user_ref.id})
        response.status_code = 201
        # response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        response = jsonify({"error": f"An Error Occurred: {e}"})
        response.status_code = 500
        # response.headers.add('Access-Control-Allow-Origin', '*')
        return response


def send_to_firebase_cloud_messaging(token, title, body):
    # See documentation on defining a message payload
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,
    )

    # Send a message to the device corresponding to the provided registration token
    response = messaging.send(message)
    # Response is a message ID string
    print('Successfully sent message:', response)