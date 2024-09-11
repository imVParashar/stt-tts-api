from fastapi import FastAPI
from app.auth.controllers import router as auth_router
from app.stt_tts.controllers import router
from app.utilities.logger import init_logger
from pydantic import BaseModel


class Settings(BaseModel):
    # Add your settings here e.g.
    # my_setting: str

    class Config:
        config_file = "../config.py"


settings = Settings()

app = FastAPI()


def create_app():
    init_logger()

    app.include_router(auth_router)
    app.include_router(router)

    return app
