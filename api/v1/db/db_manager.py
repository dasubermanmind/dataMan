
from typing import Any
from api.v1.models.node import node
from api.v1.db import database



async def add_node(payload: Any):
    query = node.insert().values(**payload.dict())

    return await database.execute(query=query)

async def get_all_nodes():
    query = node.select()
    return await database.fetch_all(query=query)

async def get_node(id):
    query = node.select(node.c.id==id)
    return await database.fetch_one(query=query)

async def delete_node(id: int):
    query = node.delete().where(node.c.id==id)
    return await database.execute(query=query)

async def update_node(id: int, payload: Any):
    query = (
        node
        .update()
        .where(node.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)