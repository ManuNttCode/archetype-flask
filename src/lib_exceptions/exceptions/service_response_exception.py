
class ServiceResponseException(Exception):
    def __init__(self, code_error, message, date, http_code):
        super().__init__(message)
        self.code_error = code_error
        self.date = date
        self.http_code = http_code
