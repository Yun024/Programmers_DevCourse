from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Citron Project API",
    description="회원 관리 시스템 API입니다.",
    version="1.0.0"
)

app.include_router(router)
