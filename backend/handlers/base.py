import requests
import logging
from typing import Literal

from asgiref.sync import sync_to_async
from core.config import Settings


settings = Settings()
logger = logging.getLogger('easy_it')


class BaseHandler:

    @sync_to_async
    def make_request(self, method: Literal['get', 'post'], prompt: str, url: str) -> requests.Response:
        try:
            # breakpoint()
            res = requests.request(
                method,
                url=url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {settings.API_KEY}"
                },
                json={
                    "model": settings.MODEL,
                    "prompt": prompt,
                    "max_tokens": 100
                })
        except Exception as error:
            logger.error(f"Request error: {error}")
        else:
            if res.status_code == 200:
                return res.json()
            return res

    async def extract_answer(self, *args, **kwargs):
        pass

    @staticmethod
    async def parse_json(*args, **kwargs):
        pass
