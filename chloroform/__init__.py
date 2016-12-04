from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object('chloroform.default_settings')
local_settings = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../cfg/settings.py"))
if 'CHLOROFORM_SETTINGS' in os.environ:
    app.config.from_envvar('CHLOROFORM_SETTINGS')
elif os.path.isfile(local_settings):
    print("loading config from {0}".format(local_settings))
    app.config.from_pyfile(local_settings)
db = SQLAlchemy(app)
from chloroform import views
