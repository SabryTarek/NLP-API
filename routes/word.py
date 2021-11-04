from fastapi import APIRouter
from models.word import Word
from config.db import conn
from schemas.word import serializeDict, serializeList
from bson import ObjectId


word = APIRouter()


@word.get('/')
async def find_all_word():
    return serializeList(conn.local.word.find())

# @word.get('/{id}')
# async def find_one_word(id):
#     return serializeDict(conn.local.word.find_one({"_id":ObjectId(id)}))


@word.post('/')
async def create_word(word: Word):
    conn.local.word.insert_one(dict(word))
    return serializeList(conn.local.word.find())


@word.put('/{id}')
async def update_word(id, word: Word):
    conn.local.word.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(word)
    })
    return serializeDict(conn.local.word.find_one({"_id": ObjectId(id)}))


@word.delete('/{id}')
async def delete_word(id, word:  Word):
    return serializeDict(conn.local.word.find_one_and_delete({"_id":  ObjectId(id)}))