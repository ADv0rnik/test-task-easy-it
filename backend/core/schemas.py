from pydantic import BaseModel
from typing import List

class Prompt(BaseModel):
    message: List[str]


class PromptGiga(BaseModel):
    message: str


class BaseResponse(BaseModel):
    id: str
    message: str

