from fastapi import FastAPI
from app.api.endpoints import router
from app.core.config import settings

app = FastAPI()

app.include_router(router)
app = FastAPI(title=settings.app_title)
