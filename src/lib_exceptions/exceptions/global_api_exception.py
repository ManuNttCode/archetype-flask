class GlobalApiException(Exception):
    def __init__(self, code_error):
        super().__init__(code_error)
        self.code_error = code_error

    @property
    def code_error(self):
        return self._code_error

    @code_error.setter
    def code_error(self, value):
        self._code_error = value