from fastapi import APIRouter
from user.model import User, collection
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.encoders import jsonable_encoder


# MongoDB connection URL
MONGO_URL = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URL)
database = client["e2echat"]

UserRouter = APIRouter(
    prefix = "/users",
    tags = ["users"]
)

# Route 1: Create new user
"""
This post route should create a new user with unique username.
After doing so, the pub/private key pair can be generated locally or 
user can upload the public key to the DB, with the signature.
"""
@UserRouter.post("/", response_model=User)
async def create_user(user: User):
    await database[collection].insert_one(user.model_dump())
    return user
    
# Route 2: List all users
"""List the users available."""
@UserRouter.get("/", response_model=list[User])
async def get_all_users():
    users = await database[collection].find({}, {"_id":0}).to_list(length=None)
    return users

# Route 3: List my friends
"""List the friends that I have ever sent a message too."""
@UserRouter.get("/friends/{username}", response_model=list)
async def get_user_friends(username: str):
    user = await database[collection].find_one({"username":username})
    friends = await database[collection].find({"username":{"$in":user["friends"]}}, {"_id":0}).to_list(length=None)
    return friends