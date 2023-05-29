import logging
from dataclasses import asdict, dataclass

VALOR_NA = "NA"
VALOR_CANAL_EVENTO = "Evento"
VALOR_CANAL_JOB = "Job"

@dataclass()
class ProcessType:
    ENTRADA: "ENTRADA"
    SALIDA: "SALIDA"
    PROCESO: "PROCESO"

@dataclass()
class NivelType:
    INFO: logging.INFO
    DEBUG = logging.DEBUG
    WARNING = logging.WARNING
    ERROR = logging.ERROR

