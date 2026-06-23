from fastapi import FastAPI
from app.database import engine,Base
from fastapi.middleware.cors import CORSMiddleware
from app.routes import jobs, auth
import os


app=FastAPI(
    title="Applysmart",
    description="AI-powered job Application Tracker",
    version="1.0.0"
)
# Add CORS middleware
allowed_origins = [
    origin.strip()
    for origin in os.getenv(
        "ALLOWED_ORIGINS",
        "http://localhost:3000,https://applysmart-frontend.onrender.com"
    ).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(jobs.router)


@app.get("/")
def root():
    return {"message":"Welcome to Applysmart API"}

app.include_router(auth.router)      # add this line

Base.metadata.create_all(bind=engine)
