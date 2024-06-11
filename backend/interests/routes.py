from flask import Blueprint, jsonify

interests_blueprint = Blueprint('interests', __name__)

@interests_blueprint.route('/submit-interests/<user_id>', methods=['POST'])
def submit_interests(user_id):
    try:
        data = request.get_json()
        interests = data.get('interests')
        if interests:
            # Update the user's interests in Firestore
            user_ref = db.collection('users').document(user_id)
            user_ref.update({'interests': firestore.ArrayUnion(interests)})
            return jsonify({"success": True}), 200
        else:
            return jsonify({"error": "No interests provided"}), 400
    except Exception as e:
        return f"An Error Occurred: {e}", 500