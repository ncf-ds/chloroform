from models.database import db

class QuestionTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template = db.Column(db.Text)
    version = db.Column(db.Integer, default = 0)
    question_group_template_id = db.Column(db.Integer, db.ForeignKey('question_group_template.id'))
    choice_templates = db.relationship('ChoiceTemplate')

    def __init__(self, template):
        self.template = template

# CREATE TABLE question_templates (
# 	id serial PRIMARY KEY,
# 	question_group_template_id int references question_group_templates(id),
# 	template text,
# 	version int DEFAULT 0
# );


