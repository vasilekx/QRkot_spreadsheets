# app/api/endpoints/donation.py
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user, current_superuser
from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.models import User
from app.schemas.donation import (
    DonationCreate,
    DonationDB,
    DonationUserDB
)
from app.services.investing import investing

router = APIRouter()


@router.get(
    '/',
    response_model=List[DonationDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_reservation(
        session: AsyncSession = Depends(get_async_session)
):
    """
    Только для суперюзеров.\n
    Возвращает список всех пожертвований.
    """
    donations = await donation_crud.get_multi(session)
    return donations


@router.post(
    '/',
    response_model=DonationUserDB,
    response_model_exclude_none=True,
)
async def create_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    """Сделать пожертвование."""
    new_donation = await donation_crud.create(
        obj_in=donation,
        session=session,
        user=user,
        commit=False,
    )
    charity_projects = await charity_project_crud.get_uninvested(session)
    if len(charity_projects) != 0:
        calculated_investments = investing(
            new_object=new_donation,
            db_objects=charity_projects,
        )
        session.add_all(calculated_investments)
    await session.commit()
    await session.refresh(new_donation)
    return new_donation


@router.get('/my', response_model=List[DonationUserDB])
async def get_my_reservations(
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):
    """Вернуть список пожертвований пользователя, выполняющего запрос."""
    user_donations = await donation_crud.get_by_user(
        user=user,
        session=session
    )
    return user_donations
