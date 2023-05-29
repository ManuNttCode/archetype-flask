import abc
import uuid

from src.lib_logs import logger_printer
from ..domain import entity_model

logger = logger_printer('ms-example', 'self', '/use_case_example')

class AbstractUseCaseRepository(abc.ABC):
    """
    Abstract class with the common operations of the entity UseCaseEntity
    """

    @abc.abstractmethod
    def add(self, entity: entity_model.UseCaseEntity) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, uuid: str) -> entity_model.UseCaseEntity:
        raise NotImplementedError


class UseCaseRepository(AbstractUseCaseRepository):
    """
    Definition of the operations that connect to database.
    """

    def __init__(self) -> None:
        self.database: list[entity_model.UseCaseEntity] = []

    def add(self, entity: entity_model.UseCaseEntity) -> bool:
        result: bool = False
        logger.log_message(nivel='INFO', mensaje='/use_case_repository.add', proceso='add operation repository')
        if entity is not None:
            result = True
            self.database.append(entity)
        return result

    def get(self, p_uuid: str) -> entity_model.UseCaseEntity:
        index = 0
        enc = False
        result: entity_model.UseCaseEntity = None
        logger.log_message(nivel='INFO', mensaje='/use_case_repository.get', proceso='add operation repository')
        while (index < len(self.database)) and not enc:
            aux: entity_model.UseCaseEntity = self.database[index]
            if aux.uuid == uuid.UUID(p_uuid):
                result = aux
                enc = True
            index += 1
        return result
