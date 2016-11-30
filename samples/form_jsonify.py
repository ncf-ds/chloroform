import os
import sys

# adding root of project to sys path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from chloroform.database import db
from chloroform.models import *
from chloroform.views import app
import json

curl = app.test_client()

def load_response(response):
    return json.loads(response.data.decode())

form = Form("Firstiest")
form.question_group = QuestionGroup("Question Group title 1")
form.question_group.questions = [Question("How much ${euphemism1} would a ${euphemism1}${euphemism2} ${euphemism2} if a ${euphemism1}${euphemism2} could ${euphemism2} ${euphemism1}?", "radio")]
form.question_group.questions[0].choices = [Choice("One Please"), Choice("No")]
form.question_group.questions[0].madlibs = [Madlib("euphemism1", "wood", "keyword"), Madlib("euphemism2", "chuck", "keyword")]
db.session.add(form)
db.session.commit()


form = Form.query.order_by(Form.id.desc()).first()    

# TODO: assert that form.jsonify() returns the values above by
#   creating single dict and referencing it on create and validate
form.jsonify()
response = load_response(curl.get('/forms/' + str(form.id) + '/edit'))
assert response['id'] == form.id
assert response['type'] == 'form'
