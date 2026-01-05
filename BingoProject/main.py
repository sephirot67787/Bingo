
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import bingo

app = FastAPI(title="Bingo Web Multiplayer")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(bingo.router)
