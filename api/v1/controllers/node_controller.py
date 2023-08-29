
from fastapi import APIRouter

from typing import Any, List
from api.v1.models.node import Node

from api.v1.db.db_manager import db_manager

node = APIRouter()

@node.get('/', response_model = List[Node])
async def index():
    return await db_manager.get_all_nodes()

@node.post('/', status_code=201)
async def add_node(payload: Any):
    node_id = await db_manager.add_node(payload)
    response = {
        'id': node_id,
        **payload.dict()
    }

    return response



