import os
import sys

# adding root of project to sys path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.database import db
from app.models import *



client = Client(name = "Simon The Pie Man")

db.session.add(client)
db.session.commit()

clients = Client.query.all()
len(clients)
# 1
clients[0].name
# "Simon The Pie Man"
