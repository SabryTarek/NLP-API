from pydantic import BaseModel

class Word(BaseModel):
    verb: str
    noun: str
    plural: str