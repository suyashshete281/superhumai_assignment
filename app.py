from fastapi import FastAPI
from routes import conference
import asyncio

app=FastAPI()




app.include_router(conference.route)

@app.get("/")
def homepage():
    return {"response":"backend system for project"}