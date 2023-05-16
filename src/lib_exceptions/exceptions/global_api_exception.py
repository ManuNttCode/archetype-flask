class GlobalApiException(Exception):
    def __init__(self, response):
        super().__init__(response)
        self.response = response