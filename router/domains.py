from fastapi import APIRouter, Request, status, Depends
from fastapi.openapi.models import APIKey
from fastapi.responses import JSONResponse
from commands import commands
from router.key import validate_api_key


# Defining our API router
def get_router(app):
    # Create a FastAPI router
    router = APIRouter()

    # Set domain
    @router.post("/domains/{app_name}/{domain_name}", response_description="Set a domain for an application")
    async def domain_set(request: Request, app_name: str, domain_name: str,
                         api_key: APIKey = Depends(validate_api_key)):
        success, message = commands.set_domain(app_name, domain_name)
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # Remove domain
    @router.delete("/domains/{app_name}/{domain_name}", response_description="Remove a domain from an application")
    async def domain_remove(request: Request, app_name: str, domain_name: str,
                            api_key: APIKey = Depends(validate_api_key)):
        success, message = commands.remove_domain(app_name, domain_name)
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # Set LetsEncrypt mail
    @router.post("/letsencrypt/{mail}", response_description="Set a mail for LetsEncrypt")
    async def letsencrypt_set_mail(request: Request, mail: str, api_key: APIKey = Depends(validate_api_key)):
        success, message = commands.set_letsencrypt_mail(mail)
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # Enable LetsEncrypt for an application
    @router.post("/letsencrypt/app/{app_name}", response_description="Enable LetsEncrypt for an application")
    async def letsencrypt_enable_app(request: Request, app_name: str,  api_key: APIKey = Depends(validate_api_key)):
        success, message = commands.enable_letsencrypt(app_name)
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # Enable LetsEncrypt automatic renewal
    @router.post("/letsencrypt/enable/auto/renewal", response_description="Enable automatic LetsEncrypt renewal")
    async def letsencrypt_enable_auto_renewal(request: Request, api_key: APIKey = Depends(validate_api_key)):
        success, message = commands.enable_letsencrypt_auto_renewal()
        content = {"success": success, "message": message}
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)

    # We return our router
    return router

