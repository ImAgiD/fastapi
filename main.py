"26.03.24==================Fastapi=================="
from fastapi import FastAPI

from app.views import router

app = FastAPI()
app.include_router(router)
