from dataclasses import dataclass
from typing import List, Optional

@dataclass()
class ErrorItem:
    name: str
    description: str
    code: Optional[str] 

@dataclass()
class ErrorCatalog:
    error_details: List[ErrorItem]
