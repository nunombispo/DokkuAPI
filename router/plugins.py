from fastapi import APIRouter, Request, status, Depends
from fastapi.openapi.models import APIKey
from fastapi.responses import JSONResponse
from commands import commands
from router.key import validate_api_key


# Defining our API router
def get_router(app):
    # Create a FastAPI router
    router = APIRouter()

    # List plugins
    @router.get("/plugins", response_description="List all plugins")
    async def list_plugins(request: Request, api_key: APIKey = Depends(validate_api_key)):
        success, message = commands.list_plugins()
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # Check if plugin is installed
    @router.get("/plugins/{plugin_name}", response_description="Check if plugin is installed")
    async def plugin_installed(request: Request, plugin_name: str,  api_key: APIKey = Depends(validate_api_key)):
        success, message = commands.is_plugin_installed(plugin_name)
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # Install plugin
    @router.post("/plugins/{plugin_name}", response_description="Install plugin")
    async def install_plugin(request: Request, plugin_name: str,  api_key: APIKey = Depends(validate_api_key)):
        success, message = commands.install_plugin(plugin_name)
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # Uninstall plugin
    @router.delete("/plugins/{plugin_name}", response_description="Uninstall plugin")
    async def uninstall_plugin(request: Request, plugin_name: str,  api_key: APIKey = Depends(validate_api_key)):
        success, message = commands.uninstall_plugin(plugin_name)
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # We return our router
    return router

