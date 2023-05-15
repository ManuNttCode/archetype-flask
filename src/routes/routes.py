import logging
from flask import request, jsonify, Blueprint
from src.lib_exceptions.exceptions.global_api_exception import GlobalApiException
from src.lib_exceptions.exceptions.service_response_exception import ServiceResponseException
from src.lib_exceptions.exceptions.validation_exception import ValidationException
from ..lib_logs import logger_printer

api = Blueprint('api', __name__, url_prefix='/api/v1')

@api.route('/', methods=['GET'])
def root():
    """
    Root entrypoint
    :return: str
    """
    logger_custom = logger_printer('ms-salesforce', 'https', 'Cloud SQL')
    logger_custom.log_message(logging.INFO, 'Mensaje de prueba', 'Payload', '202', 'self', 'Proceso')
    
    return jsonify({'result': 'Funcionando!!!'}), 200

@api.route("/global_api_exception")
def global_api_exception():
    raise GlobalApiException("GlobalApiException ha sido lanzada")

@api.route("/service_response_exception")
def service_response_exception():
    raise ServiceResponseException("ServiceResponseException ha sido lanzada", "CODE1", "2023-05-14", 500)

@api.route("/validation_exception")
def validation_exception():
    raise ValidationException("ValidationException ha sido lanzada", "CODE2")

