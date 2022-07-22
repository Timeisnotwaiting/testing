from motor.motor_asyncio import AsyncIOMotorClient as MongoClient


import config



mongo = MongoClient(config.MONGO_DB_URL)
db = mongo.PSDB

scrdb = db.scr

async def add(a: int):
    try:
        await scrdb.insert_one({"a": a})
    except:
        pass

async def pop(a: int):
    try:
        await scrdb.delete_one({"a": a})
    except:
        pass

async def target():
    users = scrdb.find({"a": {"$gt": 0}})
    users_list = []
    for user in await users.to_list(length=1000000000):
        users_list.append(user)
    return users_list
