from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import async_session
from db.repositories.profiles import ProfileRepository

async def get_db():
    async with async_session() as session:
        yield session
        await session.commit()


def get_repository(repository: ProfileRepository):
    def _get_repository(session: AsyncSession = Depends(get_db)):
        return repository(session=session)
    
    return _get_repository