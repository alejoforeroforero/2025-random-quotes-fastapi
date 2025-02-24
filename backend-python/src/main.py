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


app = FastAPI(root_path="/api")

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
app.include_router(quotes.router)
app.include_router(quotes.router, prefix="/quotes", tags=["Quotes"])


