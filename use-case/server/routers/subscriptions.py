from fastapi import APIRouter

router = APIRouter(
    prefix="/subscriptions",
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_subscriptions():
    return { "data": "database data here" }