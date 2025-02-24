from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from .database import engine
from . import models
from .routers import quotes

# Create database tables
models.Base.metadata.create_all(bind=engine)

load_dotenv()

app = FastAPI(title="Quotes API")

# CORS Configuration
origins = os.getenv("ALLOWED_ORIGINS", "").split(",")
if os.getenv("NODE_ENV") == "development":
    # Remove hardcoded localhost, use only environment variables
    pass

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

# Include routers with prefix
app.include_router(quotes.router, prefix="/api/quotes")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/")
async def root():
    return {"message": "Quotes API is running"}
