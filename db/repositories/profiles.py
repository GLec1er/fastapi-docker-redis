from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from db.tables.profiles import Profile
from schemas.profiles import ProfileRead, ProfileCreate
from typing import Optional
from db.errors import EntityNotFoundError


class ProfileRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def _get_instance(self, profile_id: UUID) -> AsyncSession:
        statement = select(Profile).where(Profile.id == profile_id)
        result = await self.session.exec(statement)
        return result.first()

    async def list(self, offset: int = 0, limit: int = 10) -> list[Profile]:
        statement = select(Profile).offset(offset).limit(limit)
        result = await self.session.exec(statement)
        return [ProfileRead(**profile.dict()) for profile in result.all()]
    
    async def create(self, profile: ProfileCreate) -> ProfileRead:
        db_profile = Profile.from_orm(profile)
        self.session.add(db_profile)
        await self.session.commit()
        await self.session.refresh(db_profile)

        return ProfileRead(**db_profile.dict())
    
    async def get(self, profile_id: UUID) -> Optional[ProfileRead]:
        db_profile = await self._get_instance(profile_id)
        if db_profile is None:
            raise EntityNotFoundError(f"Profile with id {profile_id} not found")
        
        return ProfileRead(**db_profile.dict())
    

    async def delete(self, profile_id: UUID) -> None:
        db_profile = await self._get_instance(profile_id)
        if db_profile is None:
            raise EntityNotFoundError(f"Profile with id {profile_id} not found")
        
        await self.session.delete(db_profile)
        await self.session.commit()