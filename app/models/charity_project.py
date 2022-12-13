# app/models/charity_project.py
from sqlalchemy import Column, String, Text

from app.models.base import FundBaseModel


class CharityProject(FundBaseModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return (
            f'Проект `{self.name}`. {super().__repr__()}'
        )
