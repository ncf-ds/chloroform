
from flask import Flask
from flask import request
from flask import jsonify

from app.database import db
from app import models

app = Flask(__name__)

SUCCESS_MESSAGE = "success"

def get_model_from_string(string_model):
    camelcase = ''.join(wrd.capitalize() or '_' for wrd in string_model.split('_'))
    singular = camelcase[0:-1] # just removing the final character 's'
    return getattr(models, singular)


def dump_to_json(py_object):
    if isinstance(py_object, list):        
        rows = py_object
        dict_rows= []
        for row in rows:
            row = row.__dict__
            row.pop('_sa_instance_state', None)
            dict_rows.append(row)
        return jsonify(dict_rows)
    else:
        row = py_object
        row = row.__dict__
        row.pop('_sa_instance_state', None)
        return jsonify(row)


# curl localhost:5000/clients
@app.route('/<string:model_name>')
def index(model_name):
    model = get_model_from_string(model_name)
    rows = model.query.all()
    return dump_to_json(rows)


# curl localhost:5000/clients/1
@app.route('/<string:model_name>/<int:model_id>')
def show(model_name, model_id):
    model = get_model_from_string(model_name)
    instance = model.query.get(model_id)
    return dump_to_json(instance)


# curl --data "name=new_client" localhost:5000/clients
@app.route('/<string:model_name>', methods=['POST'])
def create(model_name):
    model = get_model_from_string(model_name)
    instance = model(**request.form.to_dict())
    db.session.add(instance)
    db.session.commit()
    return jsonify({"message": SUCCESS_MESSAGE, "id": instance.id})


# curl --data "name=updated_name" localhost:5000/clients/1
@app.route('/<string:model_name>/<int:model_id>', methods=['POST', 'PUT'])
def update(model_name, model_id):
    model = get_model_from_string(model_name)
    instance = model.query.filter(model.id == model_id)
    instance.update(request.form)
    db.session.commit()
    return jsonify({"message": SUCCESS_MESSAGE})



# curl -x "DELETE" localhost:5000/clients/1
@app.route('/<string:model_name>/<int:model_id>', methods=['DELETE'])
def destroy(model_name, model_id):
    model = get_model_from_string(model_name)
    instance = model.query.filter(model.id == model_id)
    instance.delete()
    db.session.commit()
    return jsonify({"message": SUCCESS_MESSAGE})


# curl localhost:5000/form/1/edit
@app.route('/form/<int:form_id>/edit', methods=['GET'])
def edit_form_load(form_id):
    form = models.Form.query.get(form_id)
    return str(form.jsonify()) # TODO: make all jsonify()'s actually return json





