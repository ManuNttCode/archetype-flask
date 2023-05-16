from dataclasses import dataclass

@dataclass()
class ErrorDetail:
    message: str
    code: str
    http_code: int
