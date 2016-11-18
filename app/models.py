from app.database import db


class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    choice_template_id = db.Column(db.Integer, db.ForeignKey('choice_template.id'))


    def __init__(self, text):
        self.text = text



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

    def jsonify(self):
        return self.question_group.jsonify()


class Madlib(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placeholder = db.Column(db.Text)
    word = db.Column(db.Text)
    word_type = db.Column(db.Text)
    version = db.Column(db.Integer, default = 0)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

    def __init__(self, placeholder, word, word_type):
        self.placeholder = placeholder
        self.word = word
        self.word_type = word_type

    def jsonify(self):
        return {
            "text": self.text, 
            "id": self.id
        }

    


class QuestionGroup(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    version = db.Column(db.Integer, default = 0)
    title = db.Column(db.Text)
    parent_id = db.Column(db.Integer, db.ForeignKey('question_group.id'))
    question_group_template_id = db.Column(db.Integer, db.ForeignKey('question_group_template.id'))
    forms = db.relationship('Form', backref='question_group')
    questions = db.relationship('Question', backref='question')

    def __init__(self, title):
        self.title = title

    def question_groups(self):
        return QuestionGroup.query.filter(QuestionGroup.parent_id == self.id).all()

    # TODO: add proper ordering
    def children(self):
        return self.question_groups() + self.questions 

    def jsonify(self):
        return {
            "type": "question_group",
            "title": self.title,
            "children": [ child.jsonify() for child in self.children() ]
        }





class QuestionGroupTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template = db.Column(db.Text)
    version = db.Column(db.Integer, default = 0)

    def __init__(self, template):
        self.template = template



class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    question_group_id = db.Column(db.Integer, db.ForeignKey('question_group.id'))
    choices = db.relationship('Choice', backref='question')
    question_type = db.Column(db.Text)
    madlibs = db.relationship('Madlib', backref='madlib')

    def __init__(self, text, question_type):
        self.text = text
        self.question_type = question_type


    def madlibs_as_dict(self):
        new_dict = {}
        for madlib in self.madlibs:
            new_dict[madlib.placeholder] = madlib.jsonify()
        return new_dict


    def jsonify(self):
        return {
            "type": "question", 
            "text": self.text,
            "question_type": self.question_type, 
            "choices": [ choice.text for choice in self.choices ], 
            "madlibs": self.madlibs_as_dict()
        }




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


