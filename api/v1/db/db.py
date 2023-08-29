
from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from settings.settings import DATABASE_URL
from databases import Database


engine = create_engine(DATABASE_URL)
metadata = MetaData()

node = Table(
    'node',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('records', ARRAY(String)),
    Column('description', String),
    Column('created_at', String),
    Column('updated_at', String)
)

database = Database(DATABASE_URL)
