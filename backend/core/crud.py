from .schemas import Prompt
from handlers.chatgpt.gpt_handler import GPTHandler


gpt_handler = GPTHandler()


async def gpt_get_response(prompt: Prompt):
    return await gpt_handler.extract_answer(message=prompt.message)
