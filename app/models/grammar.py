
from pydantic import BaseModel
from app.models.error_type import ErrorType


# Represents the expected output of the grammar checking LLM
class llm_correction(BaseModel):
    error_type: str
    corrected_sentence: str
    