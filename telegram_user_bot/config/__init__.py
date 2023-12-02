from pydantic import BaseModel, Field


class TimeoutsConfig(BaseModel):
    before_read_seconds: int = Field(ge=0)
    before_answer_seconds: int = Field(ge=0)


class Config(BaseModel):
    api_id: int
    api_hash: str
    phone_number: str
    phone_code: int | None = None
    suvvy_api_key: str
    timeouts: TimeoutsConfig
