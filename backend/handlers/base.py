import logging
from aiohttp import ClientSession, ClientResponse

from core.config import Settings


settings = Settings()
logger = logging.getLogger('easy_it')


class BaseHandler:

    async def make_request(self, session: ClientSession, url: str, message: str) -> ClientResponse:
        try:
            async with session.post(
                    url=url,
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {settings.API_KEY}"
                    },
                    json={
                        "model": settings.MODEL,
                        "prompt": message,
                        "max_tokens": 100
                    }) as resp:
                if resp.ok:
                    return await resp.json()
                return resp
        except Exception as error:
            logger.error(f"Request error: {error}")

    async def extract_answer(self, *args, **kwargs):
        pass

    @staticmethod
    async def parse_json(*args, **kwargs):
        pass
