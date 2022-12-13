# app/models/base.py
from datetime import datetime

from sqlalchemy import (
    Column, Integer, Boolean, CheckConstraint, DateTime
)

from app.core.db import Base


class FundBaseModel(Base):
    __abstract__ = True

    full_amount = Column(
        Integer,
        CheckConstraint('full_amount > 0', name='full_amount_check'),
        nullable=False
    )
    invested_amount = Column(
        Integer,
        CheckConstraint(
            'invested_amount <= full_amount',
            name='invested_amount_check'
        ),
        default=0
    )
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)

    def __repr__(self):
        return (
            f'id={self.id}. '
            f'Инвестировано {self.invested_amount}/{self.full_amount}. '
            f'Статус: {"Закрыт" if self.fully_invested else "Открыт"}.'
        )
