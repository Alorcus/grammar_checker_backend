import json
import logging
import re
from typing import Any, List
from app.models.error_type import ErrorType
from app.schemas.exchange_schema import SentenceCorrected, TextBody
from app.services import llm_service

class GrammarService:
    @staticmethod
    def check_grammar(text: TextBody) -> List[SentenceCorrected]:
        
        sentences = GrammarService._split_text_into_sentences(text)
        
        result = []
        
        for sentence in sentences:
            response = llm_service.process_prompt(sentence)
            if response:
                parsed_response = GrammarService._parse_llm_response(sentence, response)
                if parsed_response and parsed_response.error_type != ErrorType.NOERR:
                    # Only add sentences with errors to the result
                    result.append(parsed_response)
        return result

    @staticmethod
    def _split_text_into_sentences(text: TextBody) -> List[str]:
        content = text.text

        # Use regex to split text into sentences while keeping the period
        sentences = re.findall(r'[^.!?]*[.!?]', content)
        
        # for each sentence, strip leading/trailing whitespace
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        
        return sentences
    
    @staticmethod
    def _parse_llm_response(sentence :str, response: str) -> SentenceCorrected:
        """
        Parses a JSON‐encoded string from the LLM.  Expected format:
        {
          "error_type": "<CODE>",
          "corrected_sentence": "<Corrected sentence>"
        }
        """
        logging.info("Parsing LLM response %r for sentence: %s", response, sentence)
        try:
            data: Any = json.loads(response)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON from LLM: {e.msg}") from e
        
        error_code = data["error_type"]
        corrected = data["corrected_sentence"]
        
        if error_code == "None":
            return SentenceCorrected(
                original=sentence,
                improved=sentence,
                error_type= ErrorType.NOERR)
        else:
            try:
                err_enum = ErrorType[error_code]
            except KeyError:
                # Fallback: use the raw string if it's not a known enum member
                err_enum = error_code  
            return SentenceCorrected(
                original=sentence,
                improved=corrected,
                error_type=err_enum
            )
        

        