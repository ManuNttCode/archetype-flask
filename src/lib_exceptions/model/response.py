class Response:
    def __init__(self, respuesta_servicio=None, codigo_error=None, tipo_error=None, mensaje=None, fecha_proceso=None, causas=None):
        self.respuesta_servicio = respuesta_servicio
        self.codigo_error = codigo_error
        self.tipo_error = tipo_error
        self.mensaje = mensaje
        self.fecha_proceso = fecha_proceso
        self.causas = causas or []
