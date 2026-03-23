from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Carrier Search API"
    app_version: str = "1.0.0"
    cors_origins: list[str] = ["*"]


settings = Settings()
