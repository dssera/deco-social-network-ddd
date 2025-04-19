import uvicorn

from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse


app = FastAPI()

api_router = APIRouter(prefix="/api/v1", tags=["general"])

@api_router.get("/")
async def root():
    return RedirectResponse(url="/docs", status_code=307)


@api_router.get("/healthcheck")
async def healthcheck():
    return {"status": 200}


app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)