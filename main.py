from fastapi import FastAPI
from routes.index import users
app=FastAPI()

app.include_router(users)
