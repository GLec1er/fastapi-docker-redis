from fastapi import APIRouter

from api.routes.heroes import router as heroes_router


router = APIRouter()

router.include_router(heroes_router, prefix="/heroes", tags=["heroes"])
