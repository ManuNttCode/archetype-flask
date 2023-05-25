from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional
from src.lib_exceptions.handler.util import generate_date
from src.lib_exceptions.model.error_cause import ErrorCause
from src.lib_exceptions.model.error_type import ErrorType

@dataclass
class Response:
    respuesta_servicio: str
    codigo_error: str
    tipo_error: ErrorType
    mensaje: str
    fecha_proceso: Optional[datetime] = None
    causas: Optional[ErrorCause] = None

    def to_dict(self):
        response_dict = asdict(self)
        response_dict['fecha_proceso'] = self.fecha_proceso.format() if self.fecha_proceso else None

        if isinstance(self.tipo_error, ErrorType):
            response_dict['tipo_error'] = self.tipo_error.value

        if self.causas:
            response_dict['causas'] = [cause.to_dict() for cause in self.causas]

        return response_dict
