from src.lib_exceptions.model.error_type import ErrorType

class ValidationException(Exception):
    def __init__(self, code_error, error_type=ErrorType.TECNICO.value):
        super().__init__()
        self.code_error = code_error
        self.error_type = error_type
