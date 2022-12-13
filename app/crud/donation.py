# app/crud/donation.py
from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Donation, User


class CRUDDonation(CRUDBase):
    pass

    async def get_by_user(
            self,
            user: User,
            session: AsyncSession,
    ) -> List[Donation]:
        user_donations = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id,
            )
        )
        return user_donations.scalars().all()


donation_crud = CRUDDonation(Donation)
