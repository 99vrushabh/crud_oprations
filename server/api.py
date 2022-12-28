from fastapi import FastAPI
from server.routes.user_crud import router as Router
from server.utils.create_db import migrate_db
app = FastAPI()


@app.get("/")
def home():
    return {"Welcome"}

@app.on_event("startup")
def migrate_db():
    app.include_router(Router, tags=["user"], prefix="/user/v1")
