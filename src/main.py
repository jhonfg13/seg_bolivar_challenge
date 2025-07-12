from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(
    title="Fintech Credit Advisor API",
    description="API para evaluación de créditos con IA",
    version="1.0.0"
)

# Include the router
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Fintech Credit Advisor API is running"}