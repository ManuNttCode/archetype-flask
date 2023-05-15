from flask import current_app as app, jsonify
from src.lib_exceptions.exceptions.global_api_exception import GlobalApiException
from src.lib_exceptions.exceptions.service_response_exception import ServiceResponseException
from src.lib_exceptions.exceptions.validation_exception import ValidationException


def handle_exceptions(app):
    @app.errorhandler(GlobalApiException)
    def handle_global_api_exception(error):
        response = jsonify({"code_error": error.code_error})
        return response, 500

    @app.errorhandler(ServiceResponseException)
    def handle_service_response_exception(error):
        response = jsonify({"code_error": error.code_error, "date": error.date, "http_code": error.http_code})
        return response, error.http_code

    @app.errorhandler(ValidationException)
    def handle_validation_exception(error):
        response = jsonify({"code_error": error.code_error})
        return response, 400