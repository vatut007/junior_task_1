from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = '__'

    class Config:
        env_file = '.env'


settings = Settings()
