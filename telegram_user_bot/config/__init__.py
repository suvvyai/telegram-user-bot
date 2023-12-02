from pydantic import BaseModel, Field


class TimeoutsConfig(BaseModel):
    before_read_seconds: int = Field(ge=0)
    before_answer_seconds: int = Field(ge=0)


class Config(BaseModel):
    session_name: str
    suvvy_api_key: str
    timeouts: TimeoutsConfig
