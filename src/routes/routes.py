from http.client import BAD_REQUEST
import logging
import uuid
from flask import current_app, request, jsonify, Blueprint
from src.Repository.use_case_repository import UseCaseRepository
from src.lib_exceptions.exceptions.validation_exception import ValidationException
from src.lib_exceptions.model.error_type import ErrorType
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
    p_name = request.json['name']
    p_operation = request.json['operation']
    p_operator = int(request.json['operator'])

    if not isinstance(p_name, str):
        raise ValidationException(code_error='MSRP-01')

    if not isinstance(p_operation, int):
        raise ValidationException('La operación no puede estar vacía', 'EMPTY_OPERATION')

    if not isinstance(p_operator, int):
        raise ValidationException('El operador debe ser un número', 'INVALID_OPERATOR')

    current_app.logger.info(f"Name={p_name} operation={p_operation} operator={p_operator}")

    data_request = entity_model.UseCaseRequest(uuid='',
                                               name=p_name,
                                               operation=p_operation,
                                               operator=p_operator)

    repository = UseCaseRepository()
    response_use_case = do_something(data_request, repository)

    data = jsonify({'result': response_use_case.resul})

    return data, 201