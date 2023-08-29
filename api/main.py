from fastapi import FastAPI
from api.v1.models.node import node 
from api.v1.db.db import database, metadata, engine


metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(node)
