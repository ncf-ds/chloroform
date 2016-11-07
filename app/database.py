from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from cfg import default_settings as settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
