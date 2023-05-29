import json
import os

from http.client import HTTPException
from flask import Flask, jsonify, make_response
from datetime import datetime
from werkzeug.exceptions import BadRequest

from src.lib_exceptions.exceptions.global_api_exception import GlobalApiException
from src.lib_exceptions.exceptions.service_response_exception import ServiceResponseException
from src.lib_exceptions.exceptions.validation_exception import ValidationException
from src.lib_exceptions.handler.util import from_json, generate_date

from src.lib_exceptions.model.error_cause import ErrorCause
from src.lib_exceptions.model.error_type import ErrorType
from src.lib_exceptions.model.response import Response
from src.lib_exceptions.model.service_response_model import ServiceResponseModel
from src.lib_exceptions.model.error_catalog import ErrorCatalog, ErrorItem

def handle_exceptions(app):

    @app.errorhandler(BadRequest)
    def handle_constraint_violation_exception(error):
        pass

    @app.errorhandler(ValidationException)
    def handle_validation_exception(error):
        match_error, status_code = find_response_error_catalog(error.code_error, error.error_type)
        return match_error, status_code

    @app.errorhandler(GlobalApiException)
    def handle_global_api_exception(error):
        return find_response_error_catalog(error.code_error, error.error_type)

    @app.errorhandler(ServiceResponseException)
    def handle_service_response_exception(error):
        status_code = error.http_code

        return jsonify(Response(None, codigo_error=None, tipo_error=ErrorType.TECNICO, mensaje=str(error), fecha_proceso=generate_date(), causas=[], ).to_dict()), status_code

    @app.errorhandler(Exception)
    def handle_all_exceptions(error):
        print(error)
        status_code = 500
        if isinstance(error, HTTPException):
            status_code = error.code
        
        return jsonify(Response(None, codigo_error=None, tipo_error=ErrorType.TECNICO, mensaje=str(error), fecha_proceso=generate_date(), causas=[], ).to_dict()), status_code
    
def find_response_error_catalog(code_error, error_type):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    resources_dir = os.path.join(current_dir, '../../resources')
    error_catalog_path = os.path.join(resources_dir, 'errorCatalog.json')
    process_date = generate_date()
    
    try:
        with open(error_catalog_path, 'r') as f:
            error_catalog = json.load(f, object_hook=from_json)
    except IOError as e:
        return jsonify({'error': e}), 500

    if error_catalog.error_details:
        error_detail = next((error for error in error_catalog.error_details if error.code.lower() == code_error.lower()), None)
        if error_detail:
            status = error_detail.http_code
            message = error_detail.message
            return jsonify(Response(None, code_error, error_type, message, process_date, None).to_dict()), status
    
    status_code = 500
    message = ''
    return jsonify(Response(None, code_error, error_type, message, process_date, None).to_dict()), status_code
