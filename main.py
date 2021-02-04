from fastapi import FastAPI

from user.routes import UserRouter
from conv.routes import ConvRouter

app = FastAPI()
app.include_router(ConvRouter)
app.include_router(UserRouter)

