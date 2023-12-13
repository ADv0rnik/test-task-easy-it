from pydantic import BaseModel


class Prompt(BaseModel):
    message: str


class BaseResponse(BaseModel):
    id: str
    message: str
