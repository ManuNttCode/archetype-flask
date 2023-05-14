import uuid
import logging

from flask import Flask, jsonify, request, current_app
from src.domain import entity_model
from src.repository import use_case_repository
from src.services import use_case_service
from src.lib_exceptions.handler.handler_exception import register_errorhandlers
from src.routes import register_routes


def create_app():
    app = Flask(__name__) 
    register_routes(app)
    register_errorhandlers(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)