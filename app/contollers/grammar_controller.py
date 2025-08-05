from app.schemas.exchange_schema import TextBody
from app.services.grammar_service import GrammarService
from fastapi import APIRouter

router = APIRouter()


@router.post("/grammar_check")
async def grammar_check(text: TextBody):  
    result = GrammarService.check_grammar(text)
    return result