from dataclasses import dataclass
from datetime import datetime
from src.lib_exceptions.model.error_cause import ErrorCause
from src.lib_exceptions.model.error_type import ErrorType

@dataclass()
class Response:
    respuesta_servicio: str
    codigo_error: str
    tipo_error: ErrorType
    mensaje: str
    fecha_proceso: datetime
    causas: list[ErrorCause]
