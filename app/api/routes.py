from fastapi import APIRouter

from app.core.config import APP_VERSION


router = APIRouter()


@router.get("/")
async def root():
    return {
        "message": "Welcome to File Organizer!",
        "version": APP_VERSION,
    }
