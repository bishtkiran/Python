from fastapi import FastAPI

from user_management import models
from user_management.database import engine
from user_management.routers import authentication, user

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)
