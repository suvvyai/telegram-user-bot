from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class TimeoutsConfig(BaseModel):
    before_read_seconds: int = Field(ge=0, default=0)  # TIMEOUTS__BEFORE_READ_SECONDS
    before_answer_seconds: int = Field(ge=0, default=0)  # TIMEOUTS__BEFORE_ANSWER_SECONDS
    before_typing_seconds: int = Field(ge=0, default=0)  # TIMEOUTS__BEFORE_TYPING__SECONDS


class Config(BaseSettings):
    session_name: str = "session"  # SESSION_NAME
    suvvy_api_key: str  # SUVVY_API_KEY
    timeouts: TimeoutsConfig = TimeoutsConfig()  # TIMEOUTS__...

    model_config = SettingsConfigDict(env_nested_delimiter="__")


config = Config()
