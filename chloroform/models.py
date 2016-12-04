from chloroform import db


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
    form_context_id = db.Column(db.Integer, db.ForeignKey('form_context.id'))


    def __init__(self, title):
        self.title = title

    def jsonify(self):
        return {
            "id": self.id,
            "type": "form",
            "form_question_group": self.question_group.jsonify()
        }

class Madlib(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placeholder = db.Column(db.Text)
    word = db.Column(db.Text)
    word_type = db.Column(db.Text)
    version = db.Column(db.Integer, default = 0)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    question_associations = db.relationship("QuestionMadlib", back_populates="madlib")


    def __init__(self, placeholder, word, word_type):
        self.placeholder = placeholder
        self.word = word
        self.word_type = word_type

    def jsonify(self):
        return {
            "text": self.word, 
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
        if self.id:
            return QuestionGroup.query.filter(QuestionGroup.parent_id == self.id).all()
        else:
            return []


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


class QuestionMadlib(db.Model):
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key = True)
    madlib_id = db.Column(db.Integer, db.ForeignKey('madlib.id'), primary_key = True)
    key = db.Column(db.Text)
    madlib = db.relationship('Madlib', back_populates="question_associations")
    question = db.relationship('Question', back_populates="madlib_associations")

    def __init__(self,key):
        self.key = key

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    question_group_id = db.Column(db.Integer, db.ForeignKey('question_group.id'))
    choices = db.relationship('Choice', backref='question')
    question_type = db.Column(db.Text)
    madlib_associations = db.relationship("QuestionMadlib", back_populates="question")


    def __init__(self, text, question_type):
        self.text = text
        self.question_type = question_type


    def madlibs_as_dict(self):
        new_dict = {}
        for madlib_association in self.madlib_associations:
            madlib = madlib_association.madlib
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



class FormContext(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    forms = db.relationship('Form', backref='form_context')


    def __init__(self, name):
        self.name = name


