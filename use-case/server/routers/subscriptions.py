from fastapi import APIRouter
from models.subcription import Subscription
from services.mongo_subscription_service import SubscriptionService

router = APIRouter(
    prefix="/subscriptions",
    responses={404: {"description": "Not found"}},
)

__service = SubscriptionService()

@router.get("/")
async def get_subscriptions():
    data = []
    db_subscriptions = __service.get_subscriptions()
    for d in db_subscriptions:
        data.append(Subscription(d))
    return data