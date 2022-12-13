# app/models/donation.py
from sqlalchemy import Column, Text, Integer, ForeignKey

from app.models.base import FundBaseModel


class Donation(FundBaseModel):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)

    def __repr__(self):
        return (
            f'Пожертвование {self.user_id}. {super().__repr__()}'
        )
