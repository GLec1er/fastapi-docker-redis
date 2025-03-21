from fastapi import APIRouter
from db.repositories.profiles import ProfileRepository
from db.session import async_session
from schemas.profiles import ProfileRead, ProfileCreate
from fastapi import status, Depends
from fastapi.params import Query
from typing import Optional
from typing import Dict, Any
from fastapi import Body
import random
from api.helpers.redis import cache
from uuid import UUID
import pickle
from fastapi import HTTPException
from db.errors import EntityNotFoundError

from api.helpers.repositories import get_repository


router = APIRouter()


@router.get(
    "/get_size",
    status_code=status.HTTP_200_OK,
    name="profiles_size",
)
async def get_size(
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    repository: ProfileRepository = Depends(get_repository(ProfileRepository)),
) -> Dict:
    profile_list = await repository.list(limit=limit, offset=offset)
    return {"Size": len(profile_list)}


@router.get(
    "/get_random_profile",
    status_code=status.HTTP_200_OK,
    name="profiles_get_random_profile",
)
async def get_random_profile(
    limit: int = Query(default=1, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    repository: ProfileRepository = Depends(get_repository(ProfileRepository)),
) -> Dict:
    profile_list = await repository.list(limit=limit, offset=offset)
    idx = random.randint(0, len(profile_list) - 1)

    return {
        "profile": profile_list[idx],
    }

@router.get(
    "/",
    response_model=list[Optional[ProfileRead]],
    status_code=status.HTTP_200_OK,
    name="profiles_list",
)
async def profiles(
    offset: int = 0, 
    limit: int = 10,
    repository: ProfileRepository = Depends(get_repository(ProfileRepository)),
) -> list[Optional[ProfileRead]]:
    return await repository.list(offset=offset, limit=limit)


@router.post(
    "/add",
    status_code=status.HTTP_201_CREATED,
    name="profiles_create",
    response_model=ProfileRead,
)
async def create_profile(
    profile_create: ProfileCreate = Body(...),
    repository: ProfileRepository = Depends(get_repository(ProfileRepository)),
) -> ProfileRead:
    return await repository.create(profile=profile_create)


@router.get(
    "/{profile_id}",
    response_model=ProfileRead,
    status_code=status.HTTP_200_OK,
    name="profiles_get",
)
async def get_profile(
    profile_id: UUID,
    redis_client: cache = Depends(cache),
    repository: ProfileRepository = Depends(get_repository(ProfileRepository)),
) -> ProfileRead:
    if (cached_profile := redis_client.get(f"profile_{profile_id}")) is not None:
        return pickle.loads(cached_profile)
    
    try:
        profile = await repository.get(profile_id=profile_id)
        redis_client.set(f"profile_{profile_id}", pickle.dumps(profile))
        return profile
    
    except EntityNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Profile not found"
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    

@router.delete(
    "/{profile_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="profiles_delete",
)
async def delete_profile(
    profile_id: UUID,
    redis_client: cache = Depends(cache),
    repository: ProfileRepository = Depends(get_repository(ProfileRepository)),
) -> None:
    try:
        await repository.delete(profile_id=profile_id)
        redis_client.delete(f"profile_{profile_id}")
        return {"message": "Profile deleted successfully"}
    
    except EntityNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    