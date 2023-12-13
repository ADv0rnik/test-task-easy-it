from .schemas import Prompt, BaseAnswer
from handlers.chatgpt.gpt_handler import GPTHandler
from handlers.gigachat.giga_handler import GigaHandler


gpt_handler = GPTHandler()
giga_handler = GigaHandler()


async def gpt_get_response(prompt: Prompt) -> BaseAnswer:
    return await gpt_handler.extract_answer(message=prompt.message)


async def giga_get_response(prompt: Prompt) -> BaseAnswer:
    return await giga_handler.extract_answer(message=prompt.message)
