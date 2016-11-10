from models.database import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    question_group_id = db.Column(db.Integer, db.ForeignKey('question_group.id'))
    choices = db.relationship('Choice', backref='question')

    def __init__(self, text):
        self.text = text



# CREATE TABLE questions (
# 	id serial PRIMARY KEY,
# 	question_group_id int references question_groups(id),
# 	text text
# );




