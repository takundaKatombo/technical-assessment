from flask import Blueprint, jsonify

groups_blueprint = Blueprint('groups', __name__)

@groups_blueprint.route('/get-matched-groups/<user_id>', methods=['GET'])
def get_matched_groups(user_id):
    try:
        # Retrieve user's interests from Firestore
        user_ref = db.collection('users').document(user_id)
        user_doc = user_ref.get()
        if user_doc.exists:
            user_interests = user_doc.to_dict().get('interests', [])
            # Logic to find matched groups based on interests
            # For example, query groups where 'tags' array contains any of the user's interests
            matched_groups = db.collection('groups').where('tags', 'array_contains_any', user_interests).get()
            matched_groups_data = [group.to_dict() for group in matched_groups]
            return jsonify(matched_groups_data), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return f"An Error Occurred: {e}", 500