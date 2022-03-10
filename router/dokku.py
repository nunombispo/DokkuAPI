from fastapi import APIRouter, Request, status, Body
from fastapi.responses import JSONResponse
from config import settings
from daemon import commands

# Defining our API router
def get_router(app):
    # Create a FastAPI router
    router = APIRouter()

    # We define a root path for our API with metadata
    @router.get("/", response_description="API Metadata")
    async def metadata(request: Request):
        result = {
            "api": settings.API_NAME,
            "version": settings.API_VERSION_NUMBER,
            "author": "Nuno Bispo",
            "company": "Developer Service",
            "website": "https://developer-service.io",
            "email": "developer@developer-service.io",
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)

    # Create an application
    @router.post("/app", response_description="Create an application")
    async def create_app(request: Request, app_name: str = Body(..., embed=True)):
        success, message = commands.create_app(app_name)
        return JSONResponse(status_code=status.HTTP_200_OK, content=message)

    # We return our router
    return router

