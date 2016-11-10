from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *

client = Client(name = "Simon The Pie Man")
db.session.add(client)
db.session.commit()

clients = Client.query.all()
len(clients)
# 1
clients[0].name
# "Simon The Pie Man"
