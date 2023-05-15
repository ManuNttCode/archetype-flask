from .logger_printer import LoggerPrinter

logger_printers = {}

def logger_printer(negocio=None, canal=None, consumidor=None):
    key = (negocio, canal, consumidor)
    if key not in logger_printers:
        logger_printers[key] = LoggerPrinter(*key)
    return logger_printers[key]
