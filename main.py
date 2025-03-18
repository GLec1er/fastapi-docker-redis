from fastapi import FastAPI

from api.router import router
from core.config import settings
from db.session import create_db_and_tables, bulk_create_profiles

app = FastAPI(
    title=settings.title,
    description=settings.description,
    version=settings.version,
    openapi_prefix=settings.openapi_prefix,
    openapi_url=settings.openapi_url,
    docs_url=settings.dock_url,
    redoc_url=settings.redoc_url,
)

app.include_router(router, prefix=settings.api_prefix)


@app.get('/')
def test():
    return {'text': 'Hello world'}


@app.get('/create_table')
async def create_table():
    await create_db_and_tables()
    return {'text': 'Table created'}


@app.get('/create_profiles')
async def create_profiles(number_of_profiles: int):
    await bulk_create_profiles(number_of_profiles=number_of_profiles)
    return {'text': f'{number_of_profiles} Profiles created'}
