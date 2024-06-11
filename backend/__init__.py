from flask import Flask
from backend.user.routes import user_blueprint
from backend.groups.routes import groups_blueprint
from backend.admin.routes import admin_blueprint
from backend.chat.routes import chat_blueprint
from backend.admin.routes import admin_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(groups_blueprint, url_prefix='/group')
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.register_blueprint(chat_blueprint, url_prefix='/chat')
    return app