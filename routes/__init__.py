from fastapi import APIRouter

from routes.auth import router as auth_router
from routes.tweet import router as tweet_router
from routes.user import router as user_router

router = APIRouter(prefix="/api")


router.include_router(auth_router)
router.include_router(tweet_router)
router.include_router(user_router)
