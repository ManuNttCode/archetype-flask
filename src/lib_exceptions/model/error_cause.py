from dataclasses import asdict, dataclass

@dataclass()
class ErrorCause:
    codigo_causa: str
    descripcion_causa: str

    def to_dict(self):
        return asdict(self)