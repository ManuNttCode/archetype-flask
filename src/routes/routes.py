from http.client import BAD_REQUEST
import logging
import uuid
from flask import current_app, request, jsonify, Blueprint
from src.Repository.use_case_repository import UseCaseRepository
from src.lib_exceptions.exceptions.global_api_exception import GlobalApiException
from src.lib_exceptions.exceptions.service_response_exception import ServiceResponseException
from src.lib_exceptions.exceptions.validation_exception import ValidationException
from src.lib_exceptions.model.error_catalog import ErrorItem
from src.lib_exceptions.model.error_detail import ErrorDetail
from src.lib_exceptions.model.service_response_model import ServiceResponseModel
from src.services.use_case_service import do_something
from src.domain import entity_model
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

@api.route("/use_case_example", methods=['POST'])
def do_use_case_example():
    """
    use case example

    curl --header "Content-Type: application/json" --request POST \
         --data '{"name":"xyz1", "operation":"+", "operator":"20"}' \
         http://localhost:5000/use_case_example

    :return: str
    """
    try:
        p_name = request.json['name']
        p_operation = request.json['operation']
        p_operator = int(request.json['operator'])
    except KeyError:
        error_item = ErrorItem(name='BadRequest', description='Missing required parameters')
        raise BAD_REQUEST(error_item)
    except ValueError:
        error_item = ErrorItem(name='ValidationError', description='Invalid parameter value: Expected an integer')
        raise ValidationException(error_item)

    logger_custom = logger_printer('ms-salesforce', '/use_case_example', 'front_client')

    try:
        data_request = entity_model.UseCaseRequest(uuid=uuid.UUID,
                                                name=p_name,
                                                operation=p_operation,
                                                operator=p_operator)
    except Exception as e:
        error_item = ErrorItem(name='GlobalApiError', description=str(e))
        raise GlobalApiException(error_item)

    logger_custom.log_message(logging.INFO, 'ms-example', data_request, 'CUUI123', 'operation')
    repository = UseCaseRepository()

    try:
        response_use_case = do_something(data_request, repository)
    except Exception as e:
        error_detail = ServiceResponseModel(message=str(e), http_code=500)
        raise ServiceResponseException(error_detail)

    data = jsonify({'result': response_use_case.resul})
    return data, 201