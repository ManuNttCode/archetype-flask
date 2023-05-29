import logging
import uuid as Uuid

from flask import jsonify

from src.lib_logs.logger_constants import NivelType

class LoggerPrinter:
    def __init__(self, negocio, canal, consumidor):
        self.negocio = negocio
        self.uuid = Uuid.uuid4()
        self.canal = canal
        self.consumidor = consumidor
        self.formato_log = "uuid: [%(uuid)s], tipo de proceso: %(proceso)s, mensaje: %(mensaje)s, carga_util: %(carga_util)s, canal: %(canal)s, codigo_http: %(codigo_http)s, codigo_negocio: %(codigo_negocio)s, consumidor: %(consumidor)s, negocio: %(negocio)s"
        self.logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter(self.formato_log)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_message(self, nivel='INFO', mensaje='', carga_util={}, codigo_http='200', codigo_negocio='COD01-ms-example', proceso='Api'):
        log_data = {
            "uuid": str(self.uuid),
            "proceso": proceso,
            "mensaje": mensaje,
            "carga_util": str(carga_util),
            "canal": self.canal,
            "codigo_http": codigo_http,
            "codigo_negocio": codigo_negocio,
            "consumidor": self.consumidor,
            "negocio": self.negocio
        }

        switcher = {
            'INFO': self.logger.info,
            'DEBUG': self.logger.debug,
            'WARNING': self.logger.warning,
            'ERROR': self.logger.error
        }
        log_function = switcher.get(nivel.upper())

        if log_function:
            log_function(self.formato_log, extra=log_data)