from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.api import api_router
from src.config.settings import settings
from src.utils.logger import logger

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

import os
os.makedirs("data/images", exist_ok=True)
app.mount("/data/images", StaticFiles(directory="data/images"), name="images")

@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting {settings.app_name}...")

@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.app_name}"}
