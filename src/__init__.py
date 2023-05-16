from flask import Flask

from src.lib_exceptions.handler.handler_exception import handle_exceptions
from .routes import api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    handle_exceptions(app)
    return app
