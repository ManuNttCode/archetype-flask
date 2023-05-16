from dataclasses import dataclass
from typing import List

@dataclass()
class ErrorItem:
    name: str
    description: str

@dataclass()
class ErrorCatalog:
    error_details = List[ErrorItem]
