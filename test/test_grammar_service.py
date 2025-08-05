from app.schemas.exchange_schema import TextBody
from app.services.grammar_service import GrammarService


def test_sentence_splitting():
    text = TextBody(text="This is the first sentence. This is the second sentence.")
    sentences = GrammarService._split_text_into_sentences(text)
    
    assert isinstance(sentences, list)
    assert len(sentences) == 2
    assert sentences[0] == "This is the first sentence."
    assert sentences[1] == "This is the second sentence."