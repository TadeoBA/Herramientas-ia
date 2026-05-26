from pydantic import BaseModel


class PIIFinding(BaseModel):
    type: str
    value: str
    sensitivity: str
    norm: str
