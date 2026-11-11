from fastapi import FastAPI

from app.routers.services import router as services_router

app = FastAPI(title="ServiceOps Platform API")

app.include_router(services_router)


@app.get("/health")
async def get_health_status():
    return {"status": "ok"}
