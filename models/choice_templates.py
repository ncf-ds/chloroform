from models.database import db

class ChoiceTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template = db.Column(db.Text)
    version = db.Column(db.Integer, default=0)
    question_template_id = db.Column(db.Integer, db.ForeignKey('question_template.id'))
    choices = db.relationship('Choice', backref='choice_template')

    def __init__(self, template):
        self.template = template


# CREATE TABLE choice_templates (
# 	id serial PRIMARY KEY,
# 	question_template_id int references question_templates(id),
# 	template text,
# 	version int DEFAULT 0
# );

