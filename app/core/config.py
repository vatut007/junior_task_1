from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = 'fsdfhjsgdfhsd'
    database_url: str

    model_config = SettingsConfigDict(env_file="./.env")


settings = Settings()