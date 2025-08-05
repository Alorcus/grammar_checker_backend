from app.services import llm_service
from fastapi import APIRouter

router = APIRouter()


@router.get("/initialize")
async def initialize_model():  
    llm_service.load_model()
    return {"status": "Model and tokenizer loaded successfully."}