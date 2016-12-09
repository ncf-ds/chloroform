import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from chloroform import db
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
form.form_context = FormContext(name = "CVS")
form.client = Client(name="Palermos")

#   Questions
question1 = Question("Did you find the ${name}?")
question2 = Question("Was the ${dname} full stocked and organized?")
question3 = Question("How many {$product} are on the ${dname}?")

quest_mad1 = QuestionMadlib("name")
quest_mad2 = QuestionMadlib("dname")
quest_mad3 = QuestionMadlib("product")
quest_mad4 = QuestionMadlib("dname2")

question1.choices = [Choice("Yes"),Choice("No"),Choice("Did not look")]
question1.madlib_associations = [quest_mad1]
quest_mad1.madlib = Madlib("display")

question2.choices = [Choice("Yes"),Choice("No, poorly organized"),Choice("No, not enough items")]
question2.madlib_associations = [quest_mad2]
quest_mad2.madlib = Madlib("display")

question3.choices = [Choice("Write in the number")]
question3.madlib_associations = [quest_mad3, quest_mad4]
quest_mad3.madlib = Madlib("frozen pizzas")
quest_mad4.madlib = Madlib("display")

#   Question Groups
question_group1 = QuestionGroup("QuestGroup title")
question_group2 = QuestionGroup("QuestGroup title")

question_group1.question_groups = [question_group2]

question_group2.questions = [question1, question2, question3]
# question_group1.questions = [question1]
# question_group2.questions = [question2, question3]

form.question_group = question_group1


#   Add to session
db.session.add(form)
db.session.add(question_group1)
db.session.add(question_group2)
db.session.add(question1)
db.session.add(question2)
db.session.add(question3)



# Form 2
form = Form(title="L'Oreal for CVS")
form.form_context = FormContext(name = "CVS")
form.client = Client(name="L'Oreal")

#   Questions
question1 = Question("Did you find the ${dname}?")
question2 = Question("Was the ${dname} fully stocked and organized?")
question3 = Question("How many {$product} are on the ${dname2}?")

quest_mad1 = QuestionMadlib("dname")
quest_mad2 = QuestionMadlib("dname")
quest_mad3 = QuestionMadlib("product")
quest_mad4 = QuestionMadlib("dname2")


question1.choices = [Choice("Yes"),Choice("No"),Choice("Did not look")]
question1.madlib_associations = [quest_mad1]
quest_mad1.madlib = Madlib("display")
question2.choices = [Choice("Yes"),Choice("No, poorly organized"),Choice("No, not enough items")]
question2.madlib_associations = [quest_mad2]
quest_mad2.madlib = Madlib("display")
question3.choices = [Choice("Write in the number")]
question3.madlib_associations = [quest_mad3, quest_mad4]
quest_mad3.madlib = Madlib("shampoo")
quest_mad4.madlib = Madlib("display")

#   Question Groups
question_group1 = QuestionGroup("QuestGroup title")
question_group2 = QuestionGroup("QuestGroup title")

question_group1.question_groups = [question_group2]

question_group2.questions = [question1, question2, question3]
# question_group1.questions = [question1]
# question_group2.questions = [question2, question3]

form.question_group = question_group1


#   Add to session
db.session.add(form)
db.session.add(question_group2)
db.session.add(question2)
db.session.add(question3)
db.session.add(quest_mad1)
db.session.add(quest_mad2)
db.session.add(quest_mad3)


# Form 3
form = Form(title="Palermos for Publix")
form.form_context = FormContext(name = "Publix")
form.client = Client(name="Palermos1")

#   Questions
question1 = Question("Did you find the ${name}?")
question2 = Question("Are there ${pname1} on the ${dname1}?")
question3 = Question("Are there ${pname2} on the ${dname2}?")
question4 = Question("Are there ${pname3} on the ${dname3}?")

quest_mad1 = QuestionMadlib("name")
quest_mad2 = QuestionMadlib("pname1")
quest_mad3 = QuestionMadlib("dname1")
quest_mad4 = QuestionMadlib("pname2")
quest_mad5 = QuestionMadlib("dname2")
quest_mad6 = QuestionMadlib("pname3")
quest_mad7 = QuestionMadlib("dname3")


question1.choices = [Choice("Yes"),Choice("No"),Choice("Did not look")]
question1.madlib_associations = [quest_mad1]
quest_mad1.madlib = Madlib("display")

question2.choices = [Choice("Yes, there are many items"),Choice("Yes, but there are only a few items"),Choice("No")]
question2.madlib_associations = [quest_mad2, quest_mad3]
quest_mad2.madlib = Madlib("Palermos Pepperoni Pizza")
quest_mad3.madlib = Madlib("display")

question3.choices = [Choice("Yes, there are many items"),Choice("Yes, but there are only a few items"),Choice("No")]
question3.madlib_associations = [quest_mad4, quest_mad5]
quest_mad4.madlib = Madlib("Palermos Cheese Pizza")
quest_mad5.madlib = Madlib("display")

question4.choices = [Choice("Yes, there are many items"),Choice("Yes, but there are only a few items"),Choice("No")]
question4.madlib_associations = [quest_mad6, quest_mad7] 
quest_mad6.madlib = Madlib("Palermos Sausage Pizza")
quest_mad7.madlib = Madlib("display")

#   Question Groups
question_group1 = QuestionGroup("QuestGroup title")
question_group2 = QuestionGroup("QuestGroup title")

question_group1.question_groups = [question_group2]

question_group2.questions = [question1, question2, question3, question4]
# question_group1.questions = [question1]
# question_group2.questions = [question2, question3, question4]

form.question_group = question_group1


#   Add to session
db.session.add(form)
# db.session.add(question_group2)
db.session.add(question2)
db.session.add(question3)
db.session.add(question4)
db.session.add(quest_mad1)
db.session.add(quest_mad2)
db.session.add(quest_mad3)
db.session.add(quest_mad4)
db.session.add(quest_mad5)
db.session.add(quest_mad6)
db.session.add(quest_mad7)


db.session.commit()


# form = Form.query.filter_by(title='Palermos for CVS').first()
# form.question_group
# form.question_group.questions


