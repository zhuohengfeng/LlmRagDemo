from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter(tags=["chat"], prefix="/chat")

@router.get("/")
def get_chat():
    return JSONResponse({"message": "This is chat endpoint"})