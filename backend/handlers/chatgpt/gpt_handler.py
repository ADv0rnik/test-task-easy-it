from requests import Response

from handlers.base import BaseHandler


class GPTHandler(BaseHandler):

    BASE_URL = "https://api.openai.com/v1/completions"

    async def extract_answer(self, message: str):
        json_response = await self.make_request('post', prompt=message, url=self.BASE_URL)
        return await self.parse_json(json_response)

    @staticmethod
    async def parse_json(resp: Response) -> dict:
        result = {"id": 0, "message": ""}
        if isinstance(resp, dict):
            if data := resp.get("choices", {}):
                result["message"] = data[0].get("text")
                result["id"] = resp.get("id")
                return result
            result["message"] = str(data)
            return result
        result["message"] = resp.content
        return result
