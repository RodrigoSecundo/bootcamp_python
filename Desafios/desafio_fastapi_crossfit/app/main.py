from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.api.routers import athlete_router, category_router, training_center_router

app = FastAPI(title="Desafio Crossfit API", version="1.0.0")

app.include_router(category_router)
app.include_router(training_center_router)
app.include_router(athlete_router)

add_pagination(app)
