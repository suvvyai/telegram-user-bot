from pydantic import BaseModel


class Config(BaseModel):
    api_id: int
    api_hash: str
    phone_number: str