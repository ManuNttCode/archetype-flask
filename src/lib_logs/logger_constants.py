import logging

VALOR_NA = "NA"
VALOR_CANAL_EVENTO = "Evento"
VALOR_CANAL_JOB = "Job"

class ProcessType:
    ENTRADA = "ENTRADA"
    SALIDA = "SALIDA"
    PROCESO = "PROCESO"

class NivelType:
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    WARNING = logging.WARNING
    ERROR = logging.ERROR