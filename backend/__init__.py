from flask import Flask
from user.routes import user_blueprint
from groups.routes import groups_blueprint
from admin.routes import admin_blueprint
from chat.routes import chat_blueprint
from interests.routes import interests_blueprint
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
CORS(interests_blueprint, resources={r"/user/register": {"origins": "http://127.0.0.1:3000"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# Your routes and the rest of the app setup
def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(groups_blueprint, url_prefix='/group')
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.register_blueprint(chat_blueprint, url_prefix='/chat')
    app.register_blueprint(interests_blueprint, url_prefix='/submit-interests')   
    return app