from fastapi import FastAPI
from app.database import engine,Base
from app.routes import jobs
from app.routes import jobs, auth          # add auth here


app=FastAPI(
    title="Applysmart",
    description="AI-powered job Application Tracker",
    version="1.0.0"
)

app.include_router(jobs.router)


@app.get("/")
def root():
    return {"message":"Welcome to Applysmart API"}

app.include_router(auth.router)            # add this line

Base.metadata.create_all(bind=engine)