from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from models import *

db.create_all()
