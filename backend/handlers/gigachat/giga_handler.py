from gigachat import GigaChat
from gigachat.exceptions import ResponseError


from core.config import Settings
from handlers.base import BaseHandler


settings = Settings()


class GigaHandler(BaseHandler):

    def __init__(self):
        self.creds = settings.GIGA_KEY

    async def extract_answer(self, message: str) -> dict:
        try:
            async with GigaChat(credentials=self.creds, verify_ssl_certs=False) as giga:
                resp = giga.chat(payload=message)
        except ResponseError as error:
            raise
        else:
            return await self.parse_json(resp)

    @staticmethod
    async def parse_json(response):
        result = {"id": 0, "message": "{}"}
        if response:
            data = response.choices[0].message.content
            result["id"] = str(response.created)
            result["message"] = data
            return result
        return result











