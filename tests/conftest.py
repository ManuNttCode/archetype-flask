import pytest
import os

from src import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SERVER_NAME'] = os.environ.get('SERVER_NAME', 'localhost:6060')  # Reemplaza 'localhost:5000' por tu servidor y puerto real
    return app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client