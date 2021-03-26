from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/users")


@router.get("/")
async def read_users():
    return JSONResponse({"ben": 10, "john": 5})
