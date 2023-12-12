import asyncio

from schemas import Prompt
from config import Settings


settings = Settings()


async def gpt_get_response(prompt: Prompt):
    return prompt.message
