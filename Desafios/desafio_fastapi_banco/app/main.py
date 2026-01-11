from fastapi import FastAPI

from app.core.config import settings
from app.db import init_db
from app.routers import auth, accounts

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="API bancária assíncrona com autenticação JWT, depósito, saque e extrato.",
)


@app.on_event("startup")
async def on_startup() -> None:
    await init_db()


app.include_router(auth.router)
app.include_router(accounts.router)
