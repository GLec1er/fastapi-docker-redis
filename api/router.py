from fastapi import APIRouter

from api.routes.heroes import router as heroes_router
from api.routes.profiles import router as profiles_router


router = APIRouter()

router.include_router(heroes_router, prefix="/heroes", tags=["heroes"])
router.include_router(profiles_router, prefix="/profiles", tags=["profiles"])
