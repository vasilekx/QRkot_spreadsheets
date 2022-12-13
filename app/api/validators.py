# app/api/validators.py
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models import CharityProject


async def check_name_duplicate(
        charity_project_name: str,
        session: AsyncSession,
) -> None:
    room_id = await charity_project_crud.get_charity_project_id_by_name(
        charity_project_name, session
    )
    if room_id is not None:
        raise HTTPException(
            status_code=400,
            detail='Проект с таким именем уже существует!',
        )


async def check_charity_project_exists(
        meeting_room_id: int,
        session: AsyncSession,
) -> CharityProject:
    meeting_room = await charity_project_crud.get(meeting_room_id, session)
    if meeting_room is None:
        raise HTTPException(
            status_code=404,
            detail='Проект не найден!'
        )
    return meeting_room


def check_charity_project_before_delete(
        charity_project: CharityProject
) -> None:
    if charity_project.invested_amount > 0:
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, не подлежит удалению!'
        )


def check_charity_project_fully_invested(
        fully_invested: bool,
) -> None:
    if fully_invested:
        raise HTTPException(
            status_code=400,
            detail='Закрытый проект нельзя редактировать!'
        )


def check_new_full_amount(
        new_full_amount: int,
        invested_amount: int
) -> None:
    if new_full_amount < invested_amount:
        raise HTTPException(
            status_code=422,
            detail='Нельзя установить требуемую сумму меньше уже вложенной!'
        )
