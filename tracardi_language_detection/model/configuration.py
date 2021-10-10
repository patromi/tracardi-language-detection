from pydantic import BaseModel


class Configuration(BaseModel):
    string: str
    key: str
    timeout: int = 15