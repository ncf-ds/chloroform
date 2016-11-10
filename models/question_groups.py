from models.database import db

class QuestionGroup(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    version = db.Column(db.Integer, default = 0)
    parent_id = db.Column(db.Integer, db.ForeignKey('question_group.id'))
    question_group_template_id = db.Column(db.Integer, db.ForeignKey('question_group_template.id'))
    forms = db.relationship('Form', backref='question_group')

    def __init__(self):
    	pass

# CREATE TABLE question_groups (
# 	id serial PRIMARY KEY,
# 	parent_id int references question_groups(id),
# 	question_group_template_id int references question_group_templates(id),
# 	version int DEFAULT 0
# );

