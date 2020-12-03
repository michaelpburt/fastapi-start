from fastapi import APIRouter

from doodlebug.api.endpoints import items


router = APIRouter()
router.include_router(items.router, prefix="/items", tags=["items"])
