from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
async def read_items():
    return {"user_name" : "Pierre"}

@router.get("/user_all")
async def get_all():
    return [{"user_name": "amadou"}, {"user_name": "patrick"}]