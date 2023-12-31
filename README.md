﻿## GPTChat API (Test task)

### Scope
 This is a small application for communication with different language models such as ChatGPT (by OpenAI) and GigaChat (by Sber).
 The project is using Python v.3.10 and FastAPI framework. Some extra libraries such as  `openai` and `gigachat` were used (please, check the `requirements.txt` for additional information). You might want to use docker with this application. In this case, please, make sure that docker is preinstalled on your local machine.

### Usage

1. Clone the repository onto your local machine by following command:
```commandline
git clone https://github.com/ADv0rnik/test-task-easy-it.git
```
or if you are using ssh
```commandline
git clone git@github.com:ADv0rnik/test-task-easy-it.git
```
2. Create virtual environment by using:
```commandline
python -m venv venv
```

3. Install dependencies from requirements.txt
```commandline
pip install -r requirements.txt
```

4. Setup your .env file according to .env.example schema. To use application with docker head to the next section of this manual
5. Run `python main.py` in `/backend` directory
6. To interact with endpoints go to `/gpt/v1/docs`

### Run with Docker
5. In root directory run `docker build .`
6. Once the image is built run the following command `docker run -p 8000:8000 <your_container_id>` 

### Endpoints
The following endpoints are available
#### /gpt
Request body example:
```json
{
  "message": "Proper name for a cat?"
}
```

Response body with status code 200:
```json
{
  "id": "cmpl-8VEnhnejdJ6g5lEYWRoxjXYIAVIly",
  "message": "\n\nFelix, Ginger, Misty, Simba, Tigger, Oliver, Gizmo, Coco, Charlie, Milo, Shadow, Daisy, Misty, Smokey, Lucy, Max, Kitty, Boots, Midnight, Luna, Sally, Tiger."
}
```

Response body in case of errors:
```json
{
  "id": "1702456856.73328",
  "message": "(URL('https://ngw.devices.sberbank.ru:9443/api/v2/oauth'), 400, b'{\"code\":4,\"message\":\"Can\\'t decode \\'Authorization\\' header\"}', Headers([('server', 'nginx'), ('date', 'Wed, 13 Dec 2023 08:40:58 GMT'), ('content-type', 'application/json'), ('content-length', '58'), ('connection', 'keep-alive'), ('vary', 'Origin'), ('vary', 'Access-Control-Request-Method'), ('vary', 'Access-Control-Request-Headers'), ('cache-control', 'no-cache, no-store, max-age=0, must-revalidate'), ('pragma', 'no-cache'), ('expires', '0'), ('x-content-type-options', 'nosniff'), ('strict-transport-security', 'max-age=31536000 ; includeSubDomains'), ('x-frame-options', 'DENY'), ('x-xss-protection', '1 ; mode=block'), ('referrer-policy', 'no-referrer'), ('allow', 'POST'), ('strict-transport-security', 'max-age=31536000; includeSubDomains')]))"
}
```

#### /giga
Important Note: The code is available but not tested
