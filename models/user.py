from sqlalchemy import Table,Column
from config.db import meta

users=Table(
    'users',meta,
    Column('id',int,primary_key= True),
    Column('name',str(255)),
    Column('email',str(255)),
    Column('password',str(255))
)