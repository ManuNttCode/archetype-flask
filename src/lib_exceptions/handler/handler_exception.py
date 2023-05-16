from flask import jsonify
from datetime import datetime
from werkzeug.exceptions import BadRequest

from src.lib_exceptions.exceptions.global_api_exception import GlobalApiException
from src.lib_exceptions.exceptions.service_response_exception import ServiceResponseException
from src.lib_exceptions.exceptions.validation_exception import ValidationException

from src.lib_exceptions.model.error_cause import ErrorCause
from src.lib_exceptions.model.error_type import ErrorType
from src.lib_exceptions.model.response import Response
from src.lib_exceptions.model.service_response_model import ServiceResponseModel
from src.lib_exceptions.model.error_catalog import ErrorCatalog, ErrorItem


def handle_exceptions(app):
    @app.errorhandler(BadRequest)
    def handle_constraint_violation_exception(error):
        error_item = ErrorItem(name='BadRequest', description=str(error))
        error_catalog = ErrorCatalog(error_details=[error_item])
        response_model = Response(
            respuesta_servicio=None, 
            codigo_error=None,
            tipo_error=ErrorType.TECNICO.name, 
            mensaje=str(error),
            fecha_proceso=datetime.now(), 
            causas=[ErrorCause(codigo_causa=str(error.code), descripcion_causa=str(error))]
        )
        return jsonify(response_model.__dict__), error.code

    @app.errorhandler(ValidationException)
    def handle_validation_exception(error):
        error_catalog = ErrorCatalog(error_details=[error.error_item])
        return jsonify(error_catalog.__dict__), 400

    @app.errorhandler(GlobalApiException)
    def handle_global_api_exception(error):
        error_detail = error.response
        response_model = ServiceResponseModel(
            code_error=error_detail.code, 
            date=datetime.now(), 
            http_code=error_detail.http_code, 
            message=error_detail.message, 
            type_error=ErrorType.TECNICO.value
        )
        return jsonify(response_model.__dict__), error_detail.http_code

    @app.errorhandler(ServiceResponseException)
    def handle_service_response_exception(error):
        response_model = ServiceResponseModel(
        code_error=error.code_error, 
        date=datetime.now(), 
        http_code=error.http_code, 
        message=error.message, 
        type_error=error.type_error
        )
        return jsonify(response_model.__dict__), error.http_code

    @app.errorhandler(Exception)
    def handle_all_exceptions(error):
        response_model = ServiceResponseModel(
            code_error="INTERNAL_SERVER_ERROR",
            date=datetime.now(),
            http_code=500,
            message=str(error),
            type_error=ErrorType.TECNICO.name
        )
        return jsonify(response_model.__dict__), 500
