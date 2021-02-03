from fastapi import APIRouter
from user.model import User

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
@UserRouter.post("/")
def create_user(user: User):
    
    return {"Hellow":"Wrold"}


# Route 2: List all users
"""List the users available."""
@UserRouter.get("/")
def get_all_users():
    return {"Hello": "World"}

# Route 3: List my friends
"""List the friends that I have ever sent a message too."""
@UserRouter.get("/friends/{username}")
def get_user_friends(username: str):
    return {"Hello":"World"}