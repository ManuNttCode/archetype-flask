
class ServiceResponseException(Exception):
    def __init__(self, code_error, date, http_code, message, type_error):
        super().__init__(message)
        self.code_error = code_error
        self.date = date
        self.http_code = http_code
        self.message = message
        self.type_error = type_error
