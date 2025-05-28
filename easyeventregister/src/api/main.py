from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from . import database
from .routes import router

# Ensure database tables are created
def create_db_and_tables():
    database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="EasyEventRegister Backend",
    description="Backend for event listing, details and registration"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Main API router for event and registration endpoints
app.include_router(router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# PUBLIC_INTERFACE
@app.get("/")
def health_check():
    """Health check endpoint"""
    return {"message": "Healthy"}
