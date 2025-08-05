import json
from app.models.error_type import ErrorType
from app.schemas.exchange_schema import TextBody
from app.services.grammar_service import GrammarService


def test_sentence_splitting():
    text = TextBody(text="This is the first sentence. This is the second sentence.")
    sentences = GrammarService._split_text_into_sentences(text)
    
    assert isinstance(sentences, list)
    assert len(sentences) == 2
    assert sentences[0] == "This is the first sentence."
    assert sentences[1] == "This is the second sentence."
    
    
def test_llm_response_parsing():
    sentence = "This is the wrong sentence."

    # Create a JSON string
    response = json.dumps({
        "error_type": "SVA",
        "corrected_sentence": "This is the corrected sentence."
    })
    
    parsed_response = GrammarService._parse_llm_response(sentence, response)
    
    assert parsed_response is not None
    assert parsed_response.original == sentence
    assert parsed_response.improved == "This is the corrected sentence."
    assert parsed_response.error_type == ErrorType.SVA
    
    sentence = "This is a correct sentence."
    response = json.dumps({
        "error_type": "None",
        "corrected_sentence": "This is a correct sentence."
    })
    
    parsed_response = GrammarService._parse_llm_response(sentence, response)
    
    assert parsed_response is not None
    assert parsed_response.original == sentence
    assert parsed_response.improved == sentence
    assert parsed_response.error_type == ErrorType.NOERR
    