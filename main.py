import uvicorn
import asyncio

from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse

# from common.models import test_db
from src.entrypoint.main import app_factory
from src.presentation.api.controllers.page_router import pages_router
from src.presentation.api.controllers.auth_router import auth_router

app = app_factory()


api_router = APIRouter(prefix="/api/v1", tags=["general"])

@app.get("/", tags=["General"])
async def root():
    # await test_db()
    return RedirectResponse(url="/docs", status_code=307)


@app.get("/healthcheck", tags=["General"])
async def healthcheck():
    return {"status": 200}



app.include_router(api_router)
app.include_router(pages_router)
app.include_router(auth_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8002, reload=True)