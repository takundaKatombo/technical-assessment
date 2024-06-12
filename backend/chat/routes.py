from flask import Blueprint, request, jsonify
from backend.chat.models import Message
from firebase_admin import firestore
from firebase_admin import messaging

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

chat_blueprint = Blueprint('chat', __name__)
db = firestore.client()

@chat_blueprint.route('/messages/<group_id>', methods=['GET'])
def get_messages(group_id):
    # Logic to retrieve messages for a group
    pass

# Add other chat-related routes here...