import logging
import asyncio
from aiohttp import ClientSession
from requests import Response
from datetime import datetime
from typing import List

from core.schemas import BaseResponse
from handlers.base import BaseHandler


logger = logging.getLogger("easy_it")


class GPTHandler(BaseHandler):

    BASE_URL = "https://api.openai.com/v1/completions"

    async def extract_answer(self, messages: List[str]) -> List[BaseResponse] | BaseResponse:
        responses = []
        try:
            async with ClientSession() as session:
                for message in messages:
                    resp = await self.make_request(session, self.BASE_URL, message)
                    logger.info(f"Message from GPT: {resp}, time: {datetime.now()}")
                    parsed_data = await self.parse_json(resp)
                    responses.append(BaseResponse(
                        id=parsed_data["id"],
                        message=parsed_data["message"]
                    ))                    
            return responses
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
