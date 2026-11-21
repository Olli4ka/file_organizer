from fastapi import FastAPI

from app.core.config import APP_TITLE, APP_VERSION


app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to File Organizer!",
        "version": APP_VERSION,
    }
