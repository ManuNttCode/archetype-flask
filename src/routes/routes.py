import logging
import uuid
from flask import current_app, request, jsonify, Blueprint
from src.Repository.use_case_repository import UseCaseRepository
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
    logger_custom = logger_printer('ms-salesforce', '/use_case_example', 'front_client')

    data_request = entity_model.UseCaseRequest(uuid=uuid.UUID,
                                               name=p_name,
                                               operation=p_operation,
                                               operator=p_operator)

    logger_custom.log_message(logging.INFO, 'ms-example', data_request, 'CUUI123', 'operation')

    try:
        repository = UseCaseRepository.UseCaseRepository()
        response_use_case = do_something(data_request, repository)
        data = jsonify({'result': response_use_case.resul})
        return data, 200
    except:
        assert 