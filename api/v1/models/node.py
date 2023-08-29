from typing import Any, List
from pydantic import BaseModel


class Node(BaseModel):
    name: str
    records: List[Any]
    description: str
    created_at: str
    updated_at: str

    