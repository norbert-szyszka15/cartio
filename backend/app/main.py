from fastapi import FastAPI
from sqlmodel import SQLModel

from app.db.session import engine
from app.api.router import api_router

app = FastAPI(title="Cartio API")


@app.on_event("startup")
def on_startup():
    # tworzy tabele (na start OK)
    SQLModel.metadata.create_all(engine)


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(api_router, prefix="/api")