from fastapi import APIRouter, Request, status, Depends, UploadFile, File
from fastapi.openapi.models import APIKey
from fastapi.responses import JSONResponse
from commands import commands
from router.key import validate_api_key


# Defining our API router
def get_router(app):
    # Create a FastAPI router
    router = APIRouter()

    # List application configurations
    @router.get("/config/{app_name}", response_description="List application configurations")
    async def config_show(request: Request, app_name: str, api_key: APIKey = Depends(validate_api_key)):
        success, message = commands.config_show(app_name)
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # Set application configuration key
    @router.post("/config/{app_name}/{key}/{value}", response_description="Set application configuration key (without restart)")
    async def config_set(request: Request, app_name: str, key: str, value: str,
                         api_key: APIKey = Depends(validate_api_key)):
        success, message = commands.config_set(app_name, key, value)
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # Set application configuration keys from file
    @router.post("/config/{app_name}/keys/upload/file",
                 response_description="Set application configuration keys from file (without restart)")
    async def config_file(request: Request, app_name: str,
                          file: UploadFile = File(..., description="ENV file format (key=value)"),
                          api_key: APIKey = Depends(validate_api_key)):
        contents = await file.read()
        success, message = commands.config_file(app_name, contents)
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # Apply application configuration
    @router.post("/config/{app_name}/keys/apply/restart",
                 response_description="Apply application configuration (with restart)")
    async def config_apply(request: Request, app_name: str, api_key: APIKey = Depends(validate_api_key)):
        success, message = commands.config_apply(app_name)
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # We return our router
    return router

