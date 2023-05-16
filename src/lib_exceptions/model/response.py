from dataclasses import dataclass
from datetime import datetime

@dataclass()
class Response:
    respuesta_servicio: str
    codigo_error: str
    tipo_error: str
    mensaje: str
    fecha_proceso: datetime
    causas: list[str]
