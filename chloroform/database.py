from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import configparser
config = configparser.ConfigParser()
config.read(['default.ini', 'personal.ini'])

# import logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['db']['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['db']['SQLALCHEMY_TRACK_MODIFICATIONS']
db = SQLAlchemy(app)
