import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from chloroform.database import db
from chloroform.models import *

#Things this has:
#Same client different retail chains
#Same retail chain different clients
#question_groups containing a question_group
#same qquestion_groups across forms
#Question with a free formed response

#Things this doesn't have:
#questions containing question_groups
#question_groups containing multiple question_groups

# Form 1
form = Form(title="Palermos for CVS")
form.retail_chain = RetailChain(name = "CVS")
form.client = Client(name="Palermos")

#   Questions
question1 = Question("Did you find the ${name}?")
question2 = Question("Was the ${dname} full stocked and organized?")
question3 = Question("How many {$product} are on the ${dname}?")

question1.choices = [Choice("Yes"),Choice("No"),Choice("Did not look")]
question1.madlibs = [Madlib("name","display")]
question2.choices = [Choice("Yes"),Choice("No, poorly organized"),Choice("No, not enough items")]
question2.madlibs = [Madlib("dname","display")]
question3.choices = [Choice("Write in the number")]
question3.madlibs = [Madlib("product","frozen pizzas"),Madlib("dname2","display")]

#   Question Groups
question_group1 = QuestionGroup()
question_group2 = QuestionGroup()

question_group1.question_groups = [question_group2]

question_group1.questions = [question1]
question_group2.questions = [question2, question3]

form.question_group = question_group1


#   Add to session
db.session.add(form)
db.session.add(question_group2)
db.session.add(question2)
db.session.add(question3)



# Form 2
form = Form(title="L'Oreal for CVS")
form.retail_chain = RetailChain(name = "CVS")
form.client = Client(name="L'Oreal")

#   Questions
question1 = Question("Did you find the ${dname}?")
question2 = Question("Was the ${dname} fully stocked and organized?")
question3 = Question("How many {$product} are on the ${dname2}?")

question1.choices = [Choice("Yes"),Choice("No"),Choice("Did not look")]
question1.madlibs = [Madlib("dname","display")]
question2.choices = [Choice("Yes"),Choice("No, poorly organized"),Choice("No, not enough items")]
question2.madlibs = [Madlib("dname","display")]
question3.choices = [Choice("Write in the number")]
question3.madlibs = [Madlib("product","shampoo"),Madlib("dname2","display")]

#   Question Groups
question_group1 = QuestionGroup()
question_group2 = QuestionGroup()

question_group1.question_groups = [question_group2]

question_group1.questions = [question1]
question_group2.questions = [question2, question3]

form.question_group = question_group1


#   Add to session
db.session.add(form)
db.session.add(question_group2)
db.session.add(question2)
db.session.add(question3)


# Form 3
form = Form(title="Palermos for Publix")
form.retail_chain = RetailChain(name = "Publix")
form.client = Client(name="Palermos1")

#   Questions
question1 = Question("Did you find the ${name}?")
question2 = Question("Are there ${pname1} on the ${dname1}?")
question3 = Question("Are there ${pname2} on the ${dname2}?")
question4 = Question("Are there ${pname3} on the ${dname3}?")

question1.choices = [Choice("Yes"),Choice("No"),Choice("Did not look")]
question1.madlibs = [Madlib("name","display")]
question2.choices = [Choice("Yes, there are many items"),Choice("Yes, but there are only a few items"),Choice("No")]
question2.madlibs = [Madlib("pname1","Palermos Pepperoni Pizza"),Madlib("dname1","display")]
question3.choices = [Choice("Yes, there are many items"),Choice("Yes, but there are only a few items"),Choice("No")]
question3.madlibs = [Madlib("pname2","Palermos Cheese Pizza"),Madlib("dname2","display")]
question4.choices = [Choice("Yes, there are many items"),Choice("Yes, but there are only a few items"),Choice("No")]
question4.madlibs = [Madlib("pname3","Palermos Sausage Pizza"),Madlib("dname3","display")]

#   Question Groups
question_group1 = QuestionGroup()
question_group2 = QuestionGroup()

question_group1.question_groups = [question_group2]

question_group1.questions = [question1]
question_group2.questions = [question2, question3, question4]

form.question_group = question_group1


#   Add to session
db.session.add(form)
db.session.add(question_group2)
db.session.add(question2)
db.session.add(question3)
db.session.add(question4)


db.session.commit()


# form = Form.query.filter_by(title='Palermos for CVS').first()
# form.question_group
# form.question_group.questions


