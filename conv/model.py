from pydantic import BaseModel
from typing import Union
from enum import Enum
from datetime import datetime

class MessageTypeEnum(str, Enum):
    sent = 'sent'
    received = 'received'

class Message(BaseModel):
    id: str # The id will be the same for two copies of same message. 
    text: str # Encrypted message content
    timestamp: datetime
    
    type: MessageTypeEnum #Should be either sent or received
    sender: str
    receiver: str