
# backend/tests/test_admin_routes.py
import pytest
from backend.admin.routes import admin_blueprint
from flask import Flask

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    return app

def test_admin_route(client):
    response = client.get('/admin/dashboard')  
    assert response.status_code == 200

