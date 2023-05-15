class GlobalApiException(Exception):
    def __init__(self, code_error):
        self.code_error = code_error