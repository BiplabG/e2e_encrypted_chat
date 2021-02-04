from fastapi import APIRouter
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime, timezone

from conv.model import Message, collection, MessageTypeEnum

# MongoDB connection URL
MONGO_URL = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URL)
database = client["e2echat"]

ConvRouter = APIRouter(
    prefix = "/conv",
    tags = ["conv"]
)

class SendMessageParams(BaseModel):
    sender: str
    receiver: str
    sender_text: str
    receiver_text: str

class FetchConvParameter(BaseModel):
    username: str
    friend: str
    num: int


# Route 1: Fetch last x messages of the conversation with a friend
"""Given a username, fetch last x messages from the conversation with a friend."""
@ConvRouter.post("/", response_model=list[Message])
async def get_last_messages(params: FetchConvParameter):
    messages = await database[collection].find({"$or":[{"sender":params.username, "type":MessageTypeEnum.sent}, {"receiver":params.username, "type":MessageTypeEnum.received}]}).sort("timestamp", -1).limit(params.num).to_list(length=None)
    return messages


# Route 2: Send a new message to a user
"""If the user is conversing for the first time, first verify the public key. 
Encrypt the message and send to the user."""
"""NOTE: I think a message has to be stored twice. 
Because the messages have to be encrypted for the reference of the sender, 
she has to store the message separately.
And it is going to be stored in the recipient as well."""
@ConvRouter.post("/send", response_model=Message)
async def send_new_message(params: SendMessageParams):
    id = uuid4().hex
    sender_version = Message(
        id = id,
        text = params.sender_text,
        timestamp = datetime.now(tz=timezone.utc),
        type = "sent",
        sender = params.sender,
        receiver = params.receiver,
    )
    await database[collection].insert_one(sender_version.model_dump())

    receiver_version = Message(
        id = id,
        text = params.receiver_text,
        timestamp = datetime.now(tz=timezone.utc),
        type = "received",
        sender = params.sender,
        receiver = params.receiver,
    )
    await database[collection].insert_one(receiver_version.model_dump())
    return receiver_version