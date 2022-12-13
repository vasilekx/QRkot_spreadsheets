# app/schemas/charity_project.py
from typing import Optional, Union

from pydantic import BaseModel, Field, Extra, validator

from .base import FundBaseDB


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str]
    full_amount: Optional[int]

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., max_length=100)
    description: str = Field(...)
    full_amount: int = Field(..., ge=1)


class CharityProjectUpdate(CharityProjectBase):
    pass

    @validator('*')
    def cant_be_none(cls, value: Union[str, int]):
        if value is None or value == '':
            raise ValueError('Значение не может быть пустым!')
        return value


class CharityProjectDB(FundBaseDB, CharityProjectBase):
    pass
