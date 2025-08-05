from enum import Enum

# Categorizes different types of grammatical errors that the LLM should identify.
class ErrorType(str, Enum):
    SVA   = "Subject-Verb Agreement"
    VT    = "Verb Tense Errors"
    FRAG  = "Sentence Fragments"
    RON   = "Run-On & Comma Splices"
    MD    = "Misplaced & Dangling Modifiers"
    PRON  = "Pronoun Reference & Agreement"
    PAR   = "Faulty Parallelism"
    HOMO  = "Homophone Confusion"
    APOS  = "Apostrophe Misplacement"
    PASS  = "Passive Voice Overuse"
    NOERR = "No Error"
