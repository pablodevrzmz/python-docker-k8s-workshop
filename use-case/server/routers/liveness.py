from fastapi import APIRouter
from models.subcription import Subscription
from services.mongo_subscription_service import SubscriptionService

router = APIRouter(
    prefix="/health",
)

@router.get("/")
async def get_subscriptions():
    return { "status": "ok" }