import logging

class LoggerPrinter:

    def __init__(self, negocio, uuid, canal, consumidor):
        self.negocio = negocio
        self.uuid = uuid
        self.canal = canal
        self.consumidor = consumidor
        self.formato_log = "uuid traza: %(uuid)s, tipo de proceso: %(proceso)s, mensaje: %(mensaje)s"
        self.log = logging.getLogger(__name__)

    def log(self, nivel, mensaje, carga_util, codigo_http, codigo_negocio, proceso):
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

        if nivel == logging.INFO:
            self.log.info(self.formato_log, log_data)
        elif nivel == logging.DEBUG:
            self.log.debug(self.formato_log, log_data)
        elif nivel == logging.WARNING:
            self.log.warning(self.formato_log, log_data)
        elif nivel == logging.ERROR:
            self.log.error(self.formato_log, log_data)
