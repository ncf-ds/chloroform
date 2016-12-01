from chloroform.database import db

class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    choice_template_id = db.Column(db.Integer, db.ForeignKey('choice_template.id'))


    def __init__(self, text):
        self.text = text

    def copy(self):
        new_choice    =  Choice(self.text)
        db.session.add(new_choice)
        db.session.commit()


class ChoiceTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template = db.Column(db.Text)
    version = db.Column(db.Integer, default=0)
    question_template_id = db.Column(db.Integer, db.ForeignKey('question_template.id'))
    choices = db.relationship('Choice', backref='choice_template')

    def __init__(self, template):
        self.template = template



class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    forms = db.relationship('Form', backref='client')

    def __init__(self, name):
        self.name = name




class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    version = db.Column(db.Integer, default = 0)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    question_group_id = db.Column(db.Integer, db.ForeignKey('question_group.id'))
    retail_chain_id = db.Column(db.Integer, db.ForeignKey('retail_chain.id'))


    def __init__(self, title):
        self.title = title




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

    def copy(self):
        new_madlib    =  Madlib(self.word, self.word_type)
        db.session.add(new_madlib)
        db.session.commit()


class QuestionGroup(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    version = db.Column(db.Integer, default = 0)
    parent_id = db.Column(db.Integer, db.ForeignKey('question_group.id'))
    question_group_template_id = db.Column(db.Integer, db.ForeignKey('question_group_template.id'))
    forms = db.relationship('Form', backref='question_group')

    def __init__(self):
        pass

    def copy(self):
        question_groups = [question_group.copy() for question_group in self.question_groups()]
        questions = [question.copy() for question in self.questions()]
        new_qg    =  QuestionGroup() 
        new_qg.questions = questions
        new_qg.question_groups  = question_groups
        db.session.add(new_qg)
        db.session.commit()


class QuestionGroupTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template = db.Column(db.Text)
    version = db.Column(db.Integer, default = 0)
    question_template_id = db.Column(db.Integer, db.ForeignKey('question_group_template.id'))
    def __init__(self, template):
        self.template = template



class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    question_group_id = db.Column(db.Integer, db.ForeignKey('question_group.id'))
    choices = db.relationship('Choice', backref='question')

    def __init__(self, text):
        self.text = text

    def copy(self):
        choices = [choice.copy() for choice in self.choices()]
        madlibs = [madlib.copy() for madlib in self.madlibs()]
        new_q    =  Question() 
        new_q.choices = choices
        new_q.madlibs = madlibs
        new_q.text = self.text
        db.session.add(new_q)
        db.session.commit()



class QuestionTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template = db.Column(db.Text)
    version = db.Column(db.Integer, default = 0)
    question_group_template_id = db.Column(db.Integer, db.ForeignKey('question_group_template.id'))
    choice_templates = db.relationship('ChoiceTemplate')

    def __init__(self, template):
        self.template = template



class RetailChain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    forms = db.relationship('Form', backref='retail_chain')


    def __init__(self, name):
        self.name = name


