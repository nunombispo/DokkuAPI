# Imports
from fastapi import FastAPI
from router.dokku import get_router as dokku_router

# Create the FastAPP app
app = FastAPI()

origins = [
    "*",
]


# Startup Event
@app.on_event("startup")
async def startup_db_client():
    pass


# Shutdown Event
@app.on_event("shutdown")
async def shutdown_db_client():
    pass


# Include our API router
app.include_router(dokku_router(app), tags=["Dokku"], prefix="/api")

