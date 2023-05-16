from src.lib_exceptions.model.error_detail import ErrorDetail

class ValidationException(Exception):
    def __init__(self, error_item):
        super().__init__(error_item.description)
        self.error_item = error_item
