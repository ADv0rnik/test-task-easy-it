from fastapi import APIRouter

from .crud import gpt_get_response
from .schemas import Prompt, BaseAnswer

router = APIRouter()


@router.post("/gpt")
async def gpt_response(message: Prompt) -> BaseAnswer:
    return await gpt_get_response(prompt=message)
