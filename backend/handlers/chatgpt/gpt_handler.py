from handlers.base import BaseHandler


class GPTHandler(BaseHandler):

    BASE_URL = "https://api.openai.com/v1/completions"

    async def extract_answer(self, message: str):
        return self.make_request('post', prompt=message, url=self.BASE_URL)