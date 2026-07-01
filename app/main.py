from fastapi import FastAPI

from app.database import Base, engine
from app.routers import tickets

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Support Ticket API",
    description="A cloud-native customer support ticketing API",
    version="1.0.0"
)

app.include_router(tickets.router)


@app.get("/")
def root():
    return {"message": "Support Ticket API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}