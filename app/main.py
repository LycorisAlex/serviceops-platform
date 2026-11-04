from fastapi import FastAPI

app = FastAPI(title = "ServiceOps Platform API")

@app.get("/health")
async def get_health_status():
    return {"status": "ok"}