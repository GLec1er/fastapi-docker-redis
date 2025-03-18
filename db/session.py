from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from sqlmodel import create_engine, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from core.config import settings
from db.tables.profiles import Profile


engine = create_engine(settings.sync_database_url)

async_engine = create_async_engine(settings.async_database_url, future=True)

async_session = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def create_db_and_tables() -> None:
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


async def bulk_create_profiles(number_of_profiles: int) -> None:
    fake = Faker()
    async with async_session() as session:
        for _ in range(number_of_profiles):
            profile = Profile(**fake.profile())
            session.add(profile)

        await session.commit()











