import re
from typing import List
from app.schemas.exchange_schema import SentenceCorrected, TextBody


class GrammarService:
    @staticmethod
    def check_grammar(text: TextBody) -> List[SentenceCorrected]:
        
        sentences = GrammarService._split_text_into_sentences(text)
        
        
        
        
        
        return []

    @staticmethod
    def _split_text_into_sentences(text: TextBody) -> List[str]:
        content = text.text

        # Use regex to split text into sentences while keeping the period
        sentences = re.findall(r'[^.!?]*[.!?]', content)
        
        # for each sentence, strip leading/trailing whitespace
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        
        return sentences
        