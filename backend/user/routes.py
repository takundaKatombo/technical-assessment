from flask import Flask, request, jsonify, Blueprint
from firebase_admin import firestore, credentials, initialize_app
import os

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
def register_user():
    try:
        data = request.get_json()
        # Add a new user to Firestore
        user_ref = db.collection('users').document()
        user_ref.set(data)
        return jsonify({"id": user_ref.id}), 201
    except Exception as e:
        return f"An Error Occurred: {e}", 500