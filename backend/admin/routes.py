from flask import Blueprint, jsonify

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/dashboard', methods=['GET'])
def get_dashboard_data():
    
    # Retrieve data for the admin dashboard (groups and users) from Firestore
    db = firestore.client()
    groups_data = []
    users_data = []
    
    # Get all groups
    groups_query = db.collection('groups').get()
    for group in groups_query:
        group_dict = group.to_dict()
        group_dict['id'] = group.id
        group_dict['members'] = [member['username'] for member in group_dict['members']]
        groups_data.append(group_dict)

    # Get all users
    users_query = db.collection('users').get()
    for user in users_query:
        user_dict = user.to_dict()
        user_dict['id'] = user.id
        users_data.append(user_dict)

    # Combine data into a single dictionary
    dashboard_data = {
        'users': users_data,
        'groups': groups_data
    }

# Add other admin dashboard-related routes here...