from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    default_strategy: str = "hybrid"
    cache_ttl: int = 300
    port: int = 9000
