from firebase_admin import firestore

# Initialize Firestore DB
db = firestore.client()

class Message:
    def __init__(self, text, user_id, timestamp):
        self.text = text
        self.user_id = user_id
        self.timestamp = timestamp

    def to_dict(self):
        return {
            'text': self.text,
            'user_id': self.user_id,
            'timestamp': self.timestamp,
        }

    @staticmethod
    def from_dict(source):
        # Assuming source is a Firestore document
        return Message(source.get('text'), source.get('user_id'), source.get('timestamp'))

    # Add methods to interact with Firestore if needed