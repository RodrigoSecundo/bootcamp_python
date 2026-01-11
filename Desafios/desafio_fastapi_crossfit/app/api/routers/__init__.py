from app.api.routers.athlete import router as athlete_router
from app.api.routers.category import router as category_router
from app.api.routers.training_center import router as training_center_router

__all__ = ["athlete_router", "category_router", "training_center_router"]
