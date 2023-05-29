
from datetime import date
from ..domain import entity_model
from ..Repository import use_case_repository
from src.lib_logs import logger_printer

logger = logger_printer('ms-example', 'self', '/use_case_example')

def do_something(request: entity_model.UseCaseRequest,
                 repository: use_case_repository.AbstractUseCaseRepository) -> entity_model.UseCaseResponse:
    """
    Business operation.

    :param request: entity_model.UseCaseRequest
    :param repository: use_case_repository.AbstractUseCaseRepository

    :return: entity_model.UseCaseResponse
    """

    if request is None:
        print('Request vacia')

    logger.log_message(nivel='INFO', mensaje='/use_case_service.do_something', proceso='do_someting.service')

    entity = entity_model.UseCaseEntity(uuid=request.uuid,
                                        name=request.name,
                                        operation=request.operation,
                                        operator=request.operator,
                                        date_data=date.today())

    repository.add(entity)

    return entity_model.UseCaseResponse(str(entity.calculate))
