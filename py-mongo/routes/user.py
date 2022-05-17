from fastapi import APIRouter

from bson import ObjectId
from models.user import User

from config.db import collection_name
from schemas.user import users_serializer
user_router = APIRouter()

# get
@user_router.get("/")
async def get_users():
    users = users_serializer(collection_name.find())
    return users


# post
@user_router.post("/")
async def create_user(user: User):
    _id = collection_name.insert_one(dict(user))
    return users_serializer(collection_name.find({"_id": _id.inserted_id}))


# update
@user_router.put("/{id}")
async def update_user(id: str, user: User):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })
    return users_serializer(collection_name.find({"_id": ObjectId(id)}))

# delete
@user_router.delete("/{id}")
async def delete_user(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}