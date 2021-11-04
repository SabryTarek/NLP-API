from fastapi import FastAPI
from routes.word import word
app = FastAPI()
app.include_router(word)