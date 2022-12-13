# app/crud/charity_project.py
from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):
    pass

    async def get_charity_project_id_by_name(
            self,
            charity_project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_charity_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == charity_project_name
            )
        )
        db_charity_project_id = db_charity_project_id.scalars().first()
        return db_charity_project_id

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession
    ) -> List[CharityProject]:
        projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested
            )
        )
        return sorted(
            projects.scalars().all(),
            key=lambda obj: obj.close_date - obj.create_date
        )


charity_project_crud = CRUDCharityProject(CharityProject)
