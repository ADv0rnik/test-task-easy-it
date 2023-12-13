from fastapi import APIRouter

from .crud import gpt_get_response, giga_get_response
from .schemas import Prompt, BaseAnswer

router = APIRouter()


@router.post("/gpt", response_model=BaseAnswer)
async def gpt_response(message: Prompt) -> BaseAnswer:
    return await gpt_get_response(prompt=message)


@router.post("/giga")
async def giga_response(message: Prompt) -> BaseAnswer:
    return await giga_get_response(prompt=message)
