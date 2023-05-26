from app.api.routes.cleanings import router as cleanings_router
from app.api.routes.users import router as users_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(cleanings_router, prefix="/cleanings", tags=["cleanings"])
router.include_router(users_router, prefix="/users", tags=["users"])
