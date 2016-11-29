from chloroform.database import db

class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    choice_template_id = db.Column(db.Integer, db.ForeignKey('choice_template.id'))
    searchable_field = 'text'


    def __init__(self, text):
        self.text = text


class ChoiceTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template = db.Column(db.Text)
    version = db.Column(db.Integer, default=0)
    question_template_id = db.Column(db.Integer, db.ForeignKey('question_template.id'))
    choices = db.relationship('Choice', backref='choice_template')
    searchable_field = 'template'

    def __init__(self, template):
        self.template = template



class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    forms = db.relationship('Form', backref='client')
    searchable_field = 'name'


    def __init__(self, name):
        self.name = name


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    version = db.Column(db.Integer, default = 0)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    question_group_id = db.Column(db.Integer, db.ForeignKey('question_group.id'))
    retail_chain_id = db.Column(db.Integer, db.ForeignKey('retail_chain.id'))
    searchable_field = 'title'

    def __init__(self, title):
        self.title = title
        self.searchable_field = self.title


class Madlib(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.Text)
    word_type = db.Column(db.Text)
    version = db.Column(db.Integer, default = 0)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    searchable_field = 'word'


    def __init__(self, word, word_type):
        self.word = word
        self.word_type = word_type
    

class QuestionGroup(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    version = db.Column(db.Integer, default = 0)
    parent_id = db.Column(db.Integer, db.ForeignKey('question_group.id'))
    question_group_template_id = db.Column(db.Integer, db.ForeignKey('question_group_template.id'))
    forms = db.relationship('Form', backref='question_group')

    def __init__(self):
        pass



class QuestionGroupTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template = db.Column(db.Text)
    version = db.Column(db.Integer, default = 0)
    searchable_field = 'template'

    def __init__(self, template):
        self.template = template


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    question_group_id = db.Column(db.Integer, db.ForeignKey('question_group.id'))
    choices = db.relationship('Choice', backref='question')
    searchable_field = 'text'

    def __init__(self, text):
        self.text = text



class QuestionTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template = db.Column(db.Text)
    version = db.Column(db.Integer, default = 0)
    question_group_template_id = db.Column(db.Integer, db.ForeignKey('question_group_template.id'))
    choice_templates = db.relationship('ChoiceTemplate')
    searchable_field = 'template'

    def __init__(self, template):
        self.template = template



class RetailChain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    forms = db.relationship('Form', backref='retail_chain')
    searchable_field = 'name'



    def __init__(self, name):
        self.name = name

