from models.database import db

class Madlib(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.Text)
    word_type = db.Column(db.Text)
    version = db.Column(db.Integer, default = 0)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

    def __init__(self, word, word_type):
        self.word = word
        self.word_type = word_type

	
# CREATE TABLE madlibs (
# 	id serial PRIMARY KEY,
# 	client_id int references clients(id),
# 	question_id int references questions(id),
# 	word text,
# 	type text
# );

# CREATE TABLE madlibs_questions (
# 	madlib_id int references madlibs(id),
# 	question_id int references questions(id),
# 	PRIMARY KEY(madlib_id, question_id)
# );

# CREATE TABLE madlibs_forms (
# 	madlib_id int references madlibs(id),
# 	form_id int references forms(id),
# 	PRIMARY KEY(madlib_id, form_id)
# );
