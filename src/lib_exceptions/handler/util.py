from datetime import datetime
from src.lib_exceptions.model.error_catalog import ErrorCatalog
from src.lib_exceptions.model.error_detail import ErrorDetail


def generate_date():
        date_format = "%d-%m-%Y %H:%M:%S"
        current_time = datetime.now()
        return current_time.strftime(date_format)

def from_json(json_object):
    if 'error_details' in json_object:
        return ErrorCatalog([ErrorDetail(**detail) for detail in json_object['error_details']])
    return json_object