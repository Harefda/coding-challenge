from fastapi import FastAPI

app = FastAPI()


@app.get("/main")
def return_hello():
    return{"ping": "pong"}

from models import views

app.include_router(views.router)