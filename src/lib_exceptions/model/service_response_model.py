class ServiceResponseModel:
    def __init__(self, code_error=None, date=None, http_code=None, message=None, type_error=None):
        self.code_error = code_error
        self.date = date
        self.http_code = http_code
        self.message = message
        self.type_error = type_error
