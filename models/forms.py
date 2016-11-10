from models.database import db

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    version = db.Column(db.Integer, default = 0)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    question_group_id = db.Column(db.Integer, db.ForeignKey('question_group.id'))
    retail_chain_id = db.Column(db.Integer, db.ForeignKey('retail_chain.id'))


    def __init__(self, title):
        self.title = title


# CREATE TABLE forms (
# 	id serial PRIMARY KEY,
# 	client_id int references clients(id),
# 	question_group_id int references question_groups(id),
# 	retail_chain_id int references retail_chains(id),
# 	title text,
# 	version int DEFAULT 0
# );
