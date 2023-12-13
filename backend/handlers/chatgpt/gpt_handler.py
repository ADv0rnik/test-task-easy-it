import logging
from requests import Response
from datetime import datetime

from core.schemas import BaseResponse
from handlers.base import BaseHandler


logger = logging.getLogger("easy_it")


class GPTHandler(BaseHandler):

    BASE_URL = "https://api.openai.com/v1/completions"

    async def extract_answer(self, message: str) -> BaseResponse:
        try:
            json_response = await self.make_request('post', prompt=message, url=self.BASE_URL)
            base_resp = await self.parse_json(json_response)
            logger.info(f"Message from GPT: {base_resp}, time: {datetime.now()}")
            return BaseResponse(
                id=base_resp["id"],
                message=base_resp["message"]
            )
        except Exception as error:
            logger.error(f"Exception raised: {error}")
            return BaseResponse(
                id=str(datetime.timestamp(datetime.now())),
                message=str(error)
            )

    @staticmethod
    async def parse_json(resp: Response) -> dict:
        result = {
            "id": str(datetime.timestamp(datetime.now())),
            "message": "{}"
        }
        if isinstance(resp, dict):
            if data := resp.get("choices", {}):
                result["message"] = data[0].get("text")
                result["id"] = resp.get("id")
                return result
            return result
        result["message"] = resp.content
        return result
