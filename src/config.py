from pathlib import Path
from typing import Literal

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent

class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "src" / "auth" / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "src" / "auth" / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30
    # refresh_token_expire_minutes: int = 60 * 24 * 30
    # access_token_expire_minutes: int = 3

class Settings(BaseSettings):
    # Settings
    MODE: Literal["DEV", "TEST", "PROD"]
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"

    DATABASE_URL: str
    TEST_DB_URL: str

    ## JWT HS256
    SECRET_KEY: str
    ALGORITHM: str

    ## JWT RS256 (RSA)
    auth_jwt: AuthJWT = AuthJWT()

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
