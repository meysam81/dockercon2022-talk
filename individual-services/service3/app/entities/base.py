from pydantic import BaseModel as _PydanticBaseModel


class BaseModel(_PydanticBaseModel):
    class Config:
        orm_mode = True
