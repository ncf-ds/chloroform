from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
import sys

# adding root of project to sys path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.database import db

db.create_all()
db.session.commit()