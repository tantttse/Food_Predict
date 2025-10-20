from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.predict import router as predict_router
from app.api.heath import router as health_router
from app.db.session import enable_unaccent_extension
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Food Prediction API",
    version="ai-v1",
    openapi_version="3.0.3",
    servers=[
        {"url": "https://foodpredict-production-ac70.up.railway.app", "description": "Production API"},
        {"url": "http://127.0.0.1:8000", "description": "FastAPI Local"},
        {"url": "http://localhost:8000", "description": "FastAPI Localhost"},
        {"url": "http://localhost:5013", "description": "C# API"}
    ]
)

enable_unaccent_extension()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(predict_router)
app.include_router(health_router)
