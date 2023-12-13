import logging

from datetime import datetime
from gigachat import GigaChat
from gigachat.exceptions import ResponseError


from core.config import Settings
from core.schemas import BaseResponse
from handlers.base import BaseHandler


settings = Settings()
logger = logging.getLogger("easy_it")


class GigaHandler(BaseHandler):

    def __init__(self):
        self.creds = settings.GIGA_KEY

    async def extract_answer(self, message: str) -> BaseResponse:
        try:
            async with GigaChat(credentials=self.creds, verify_ssl_certs=False) as giga:
                resp = giga.chat(payload=message)
        except ResponseError as error:
            logger.error(f"Response error {error}")
            base_resp = BaseResponse(
                id=str(datetime.timestamp(datetime.now())),
                message=str(error)
            )
            return base_resp
        else:
            logger.info(f"Response from Giga: {resp}")
            base_resp = await self.parse_json(resp)
            return BaseResponse(
                id=base_resp["id"],
                message=base_resp["message"]
            )

    @staticmethod
    async def parse_json(response):
        result = {"id": 0, "message": "{}"}
        if response:
            data = response.choices[0].message.content
            result["id"] = str(response.created)
            result["message"] = str(data)
            return result
        return result
