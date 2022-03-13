from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from commands import commands


# Defining our API router
def get_router(app):
    # Create a FastAPI router
    router = APIRouter()

    # List all applications
    @router.get("/apps", response_description="List all applications")
    async def list_apps(request: Request):
        success, message = commands.list_apps()
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # Create an application
    @router.post("/apps/{app_name}", response_description="Create an application")
    async def create_app(request: Request, app_name: str):
        success, message = commands.create_app(app_name)
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # Delete an application
    @router.delete("/apps/{app_name}", response_description="Delete an application")
    async def delete_app(request: Request, app_name: str):
        success, message = commands.delete_app(app_name)
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # We return our router
    return router

