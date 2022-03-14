from fastapi import Security, HTTPException
from fastapi.security import APIKeyQuery, APIKeyHeader, APIKeyCookie
from starlette.status import HTTP_403_FORBIDDEN
from config import settings

API_KEY = settings.API_KEY


# Validate API key
def validate_api_key(
        api_key_header: str = Security(APIKeyHeader(name='API-KEY', auto_error=False))):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid or missing API key")
