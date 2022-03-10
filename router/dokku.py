from fastapi import APIRouter, Request, status, Body
from fastapi.responses import JSONResponse
from config import settings
from daemon import commands

# Defining our API router
from router.models import AppModel


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
    @router.post("/apps", response_description="Create an application")
    async def create_app(request: Request, app_model: AppModel):
        success, message = commands.create_app(app_model.name)
        content = {"success": success, "message": message}
        if success:
            return JSONResponse(status_code=status.HTTP_200_OK, content=content)
        else:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=content)

    # Delete an application
    @router.delete("/apps", response_description="Delete an application")
    async def delete_app(request: Request, app_model: AppModel):
        success, message = commands.delete_app(app_model.name)
        content = {"success": success, "message": message}
        if success:
            return JSONResponse(status_code=status.HTTP_200_OK, content=content)
        else:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=content)

    # List all applications
    @router.get("/apps", response_description="List all applications")
    async def list_apps(request: Request):
        success, message = commands.list_apps()
        content = {"success": success, "message": message}
        if success:
            return JSONResponse(status_code=status.HTTP_200_OK, content=content)
        else:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=content)

    # We return our router
    return router

