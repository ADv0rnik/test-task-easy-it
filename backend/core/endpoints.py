from fastapi import APIRouter

from .crud import gpt_get_response, giga_get_response
from .schemas import Prompt, BaseResponse

router = APIRouter()


@router.post("/gpt", response_model=BaseResponse)
async def gpt_response(message: Prompt) -> BaseResponse:
    return await gpt_get_response(prompt=message)


@router.post("/giga", response_model=BaseResponse)
async def giga_response(message: Prompt) -> BaseResponse:
    return await giga_get_response(prompt=message)
