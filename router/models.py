from pydantic import BaseModel


class AppModel(BaseModel):
    name: str

