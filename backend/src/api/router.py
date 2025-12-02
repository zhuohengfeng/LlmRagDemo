from fastapi import APIRouter
from .v1 import (
    chat_router
)

router = APIRouter(prefix="/api")

# v1版本的api，如果有需要后面可以增加v2等版本
router_v1 = APIRouter(prefix="/v1")
router_v1.include_router(chat_router)

router.include_router(router_v1)
