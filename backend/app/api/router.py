from fastapi import APIRouter
from app.modules.items.router import router as items_router

api_router = APIRouter()
api_router.include_router(items_router, prefix="/items", tags=["items"])
