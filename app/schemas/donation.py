# app/schemas/donation.py
from typing import Optional

from pydantic import BaseModel, Field, Extra

from .base import BaseDB, FundBaseDB


class DonationBase(BaseModel):
    full_amount: int = Field(None, ge=1)
    comment: Optional[str]

    class Config:
        extra = Extra.forbid


class DonationCreate(DonationBase):
    full_amount: int = Field(..., ge=1)


class DonationDB(FundBaseDB, DonationCreate):
    user_id: int


class DonationUserDB(BaseDB, DonationCreate):
    pass
