from fastapi import APIRouter
import routers.subscriptions as subscriptions

router = APIRouter()
router.include_router(subscriptions.router)