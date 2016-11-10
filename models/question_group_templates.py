from models.database import db

class QuestionGroupTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template = db.Column(db.Text)
    version = db.Column(db.Integer, default = 0)

    def __init__(self, template):
        self.template = template


# CREATE TABLE question_group_templates (
# 	id serial PRIMARY KEY,
# 	template text,
# 	version int DEFAULT 0
# );