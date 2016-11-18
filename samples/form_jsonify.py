import os
import sys

# adding root of project to sys path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.database import db
from app.models import *


form = Form("Firstiest")
form.question_group = QuestionGroup("Question Group title 1")
form.question_group.questions = [Question("How much ${euphemism1} would a ${euphemism1}${euphemism2} ${euphemism2} if a ${euphemism1}${euphemism2} could ${euphemism2} ${euphemism1}?", "radio")]
form.question_group.questions[0].choices = [Choice("One Please"), Choice("No")]
form.question_group.questions[0].madlibs = [Madlib("euphemism1", "wood", "keyword"), Madlib("euphemism2", "chuck", "keyword")]
db.session.add(form)
db.session.commit()


form = Form.query.order_by(Form.id.desc()).first()    
form.jsonify()