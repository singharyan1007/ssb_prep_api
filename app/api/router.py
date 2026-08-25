from fastapi import APIRouter

from app.api.routers import admin, auth, config, current_affairs, ingest

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(config.router, prefix="/config", tags=["config"])
api_router.include_router(current_affairs.router, prefix="/current-affairs", tags=["current-affairs"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])
api_router.include_router(ingest.router, prefix="/internal", tags=["internal"])
