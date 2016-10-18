from models.database import db

class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    choice_template_id = db.Column(db.Integer, db.ForeignKey('choice_template.id'))


    def __init__(self, text):
        self.text = text


# CREATE TABLE choices (
# 	id serial PRIMARY KEY,
# 	question_id int references questions(id),
# 	choice_template_id int references choice_templates(id),
# 	text text
# );
