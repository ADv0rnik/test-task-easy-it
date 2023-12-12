import requests

api_key="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"

def chat_with_chatgpt(prompt):
    res = requests.request(
        'post',
        f"https://api.openai.com/v1/completions",
        headers={
              "Content-Type": "application/json",
              "Authorization": f"Bearer {api_key}"
        },
        json={
              "model": "text-davinci-003",
              "prompt": prompt,
              "max_tokens": 100
        })
    return res.json()


print(chat_with_chatgpt("What time is it in Canada?"))
