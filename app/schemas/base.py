# app/schemas/base.py
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseDB(BaseModel):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class FundBaseDB(BaseDB):
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime]
