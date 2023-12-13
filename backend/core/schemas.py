from pydantic import BaseModel


class Prompt(BaseModel):
    message: str


class BaseAnswer(BaseModel):
    id: str
    message: str
