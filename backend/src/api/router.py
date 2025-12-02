from fastapi import APIRouter
from .v1 import (
    chat_router
)

router = APIRouter(prefix="/api")

router.include_router(chat_router)