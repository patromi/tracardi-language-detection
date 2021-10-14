from pydantic import BaseModel
from tracardi.domain.entity import Entity


class Data(BaseModel):
    string: str
    key: str
    timeout: int = 15


class Config(BaseModel):
    source: Entity
