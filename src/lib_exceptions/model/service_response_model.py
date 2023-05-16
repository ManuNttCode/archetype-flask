from dataclasses import dataclass
from datetime import datetime

@dataclass()
class ServiceResponseModel:
    code_error: str
    date: datetime
    http_code: str
    message: str
    type_error: str
