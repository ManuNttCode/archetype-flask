import logging
import uuid as Uuid

from src.lib_logs.logger_constants import NivelType

class LoggerPrinter:

    def __init__(self, negocio, canal, consumidor):
        self.negocio = negocio
        self.uuid = Uuid.uuid4()
        self.canal = canal
        self.consumidor = consumidor
        self.formato_log = "uuid traza: %(uuid)s, tipo de proceso: %(proceso)s, mensaje: %(mensaje)s"
        self.logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter(self.formato_log)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    

    def log_message(self, nivel=NivelType, mensaje='', carga_util={}, codigo_http='200', codigo_negocio='ms-example', proceso='Api'):
        log_data = {
            "uuid": self.uuid,
            "proceso": proceso,
            "mensaje": mensaje,
            "carga_util": carga_util,
            "canal": self.canal,
            "codigo_http": codigo_http,
            "codigo_negocio": codigo_negocio,
            "consumidor": self.consumidor,
            "negocio": self.negocio
        }

        switcher = {
        logging.INFO: self.logger.info,
        logging.DEBUG: self.logger.debug,
        logging.WARNING: self.logger.warning,
        logging.ERROR: self.logger.error
        }
        log_function = switcher.get(nivel)
        if log_function:
            log_function(self.formato_log % log_data)
