from pydantic import BaseSettings


class Settings(BaseSettings):
    example_var: str
    development: bool = False


settings = Settings()
