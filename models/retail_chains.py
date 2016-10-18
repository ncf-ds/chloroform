from models.database import db

class RetailChain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    forms = db.relationship('Form', backref='retail_chain')


    def __init__(self, name):
        self.name = name


# CREATE TABLE retail_chains (
# 	id serial PRIMARY KEY,
# 	name text
# );
