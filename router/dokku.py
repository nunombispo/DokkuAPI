from fastapi import APIRouter, Request, status, Body
from fastapi.responses import JSONResponse
from config import settings
from commands import commands


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

    # List all applications
    @router.get("/apps", response_description="List all applications")
    async def list_apps(request: Request):
        success, message = commands.list_apps()
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # List plugins
    @router.get("/plugins", response_description="List all plugins")
    async def list_plugins(request: Request):
        success, message = commands.list_plugins()
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # Check if plugin is installed
    @router.get("/plugins/{plugin}", response_description="Check if plugin is installed")
    async def is_plugin_installed(request: Request, plugin: str):
        success, message = commands.is_plugin_installed(plugin)
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # Install plugin
    @router.post("/plugins/{plugin}", response_description="Install plugin")
    async def install_plugin(request: Request, plugin: str):
        success, message = commands.install_plugin(plugin)
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # Uninstall plugin
    @router.delete("/plugins/{plugin}", response_description="Uninstall plugin")
    async def uninstall_plugin(request: Request, plugin: str):
        success, message = commands.uninstall_plugin(plugin)
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # We return our router
    return router

