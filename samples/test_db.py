from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.models import *

client = Client(name = "L'Oreal")
db.session.add(client)
db.session.commit()

clients = Client.query.all()
len(clients)
# 1
clients[0].name
# "L'Oreal"
