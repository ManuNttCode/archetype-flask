from http.client import BAD_REQUEST
import uuid
from flask import current_app, request, jsonify, Blueprint
from src.Repository.use_case_repository import UseCaseRepository
from src.lib_exceptions.exceptions.validation_exception import ValidationException
from src.services.use_case_service import do_something
from src.lib_logs import logger_printer

from src.domain import entity_model
from ..lib_logs import logger_printer

api = Blueprint('api', __name__, url_prefix='/api/v1')
logger = logger_printer('ms-example', 'https', 'client-examples')

@api.route('/', methods=['GET'])
def root():
    """
    Root entrypoint
    :return: str
    """
    return jsonify({'result': 'working...'}), 200

@api.route("/use_case_example", methods=['POST'])
def do_use_case_example():
    """
    use case example

    curl --header "Content-Type: application/json" --request POST \
         --data '{"name":"xyz1", "operation":"+", "operator":"20"}' \
         http://localhost:5000/use_case_example

    :return: str
    """
    p_name = request.json['name']
    p_operation = request.json['operation']
    p_operator = request.json['operator']

    if not p_name or not isinstance(p_name, str):
        logger.log_message(nivel='ERROR', mensaje='El parámetro "name" no es correcto', carga_util={'name': p_name}, codigo_http='422', proceso='request')
        raise ValidationException(code_error='MSRP-01')

    if not p_operation or not isinstance(p_operation, str):
        logger.log_message(nivel='ERROR', mensaje='El parámetro "operation" no es correcto', carga_util={'operation': p_operation}, codigo_http='422', proceso='request')
        raise ValidationException(code_error='MSRP-01')

    if not p_operator or not isinstance(p_operator, int):
        logger.log_message(nivel='ERROR', mensaje='El parámetro "operator" no es correcto', carga_util={'operator': p_operator}, codigo_http='422', proceso='request')
        raise ValidationException(code_error='MSRP-01')

    logger.log_message(nivel='INFO', mensaje='request in progress', proceso='request')
    data_request = entity_model.UseCaseRequest(uuid='',
                                               name=p_name,
                                               operation=p_operation,
                                               operator=p_operator)

    repository = UseCaseRepository()
    response_use_case = do_something(data_request, repository)
    logger.log_message(nivel='INFO', mensaje='success request', codigo_http='201', proceso='request')

    data = jsonify({'result': response_use_case.resul})
    return data, 201