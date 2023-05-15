class ErrorDetail:
    def __init__(self, message=None, code=None, http_code=None):
        self.message = message
        self.code = code
        self.http_code = http_code
