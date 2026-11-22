from fastapi import FastAPI

from app.api.routes import router
from app.core.config import APP_TITLE, APP_VERSION


app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
)

app.include_router(router)
