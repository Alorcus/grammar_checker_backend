from app.controllers import internal_controller
from fastapi import FastAPI
from .controllers import grammar_controller

app = FastAPI()

app.include_router(grammar_controller.router, prefix="/grammar")
app.include_router(internal_controller.router, prefix="/internal")
