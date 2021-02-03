from fastapi import FastAPI

from user.routes import UserRouter

app = FastAPI()
app.include_router(UserRouter)

