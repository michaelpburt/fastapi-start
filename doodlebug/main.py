from fastapi import FastAPI

from doodlebug.api import api

app = FastAPI(
    title="doodlebug", openapi_url="/openapi.json"
)

app.include_router(api.router, prefix="/v1")
