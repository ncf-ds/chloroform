from models.database import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    forms = db.relationship('Form', backref='client')

    def __init__(self, name):
        self.name = name

    # def __repr__(self):
    #     return '<Client %r>' % self.name


# CREATE TABLE clients (
# 	id serial PRIMARY KEY,
# 	name text
# );