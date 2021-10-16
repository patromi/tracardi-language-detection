from pydantic import BaseModel
from tracardi.domain.entity import Entity


class Message(BaseModel):
    message: str


class Key(BaseModel):
    token: str


class Configuration(BaseModel):
    source: Entity
