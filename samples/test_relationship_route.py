import os
import sys

# adding root of project to sys path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from chloroform.routes import app
from chloroform.database import db
from chloroform.models import *
import json

curl = app.test_client()

group = QuestionGroup()
question = Question("test question")

db.session.add(group)
db.session.add(question)
db.session.commit()

curl.post('/question_groups/{}/questions/{}'.format(group.id, question.id))

group = QuestionGroup.query.get(group.id)

assert group.questions[0] == question
