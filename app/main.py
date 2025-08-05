from fastapi import FastAPI
from .controllers import grammar_controller

app = FastAPI()

app.include_router(grammar_controller.router, prefix="/grammar")
