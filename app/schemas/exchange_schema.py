from pydantic import BaseModel
from app.models.error_type import ErrorType

class TextBody(BaseModel):
    text : str

class SentenceCorrected(BaseModel):
    original: str
    improved: str
    type: ErrorType
