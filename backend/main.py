import logging

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.config import Settings, LOGGING_CONFIG
from core.endpoints import router


settings = Settings()
logging.config.dictConfig(LOGGING_CONFIG)


def start_application(config: Settings):
    application = FastAPI(
        title=config.PROJECT_NAME,
        version=config.PROJECT_VERSION,
        description="request to chatgpt",
        docs_url=f"{config.API_V1_STR}/docs",
        redoc_url=f"{config.API_V1_STR}/redoc",
        debug=True
    )
    return application


app = start_application(settings)

app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGIN,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=int(settings.PORT),
        host=settings.PROJECT_HOST,
        reload=True
    )
