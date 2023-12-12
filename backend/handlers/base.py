import requests
from typing import Literal
from core.config import Settings
#
#
settings = Settings()


class BaseHandler:
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
                    "model": "text-davinci-003",
                    "prompt": prompt,
                    "max_tokens": 100
                })
            return res.json()
        except Exception as error:
            return error


