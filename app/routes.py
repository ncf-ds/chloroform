from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

from app import models

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

# curl localhost:5000/clients/new
@app.route('/<string:model_name>/new', methods=['GET'])
def new(model_name):
    return 'render new form for ' + model_name + '\n'

# curl --data "name=new_client" localhost:5000/clients
@app.route('/<string:model_name>', methods=['POST'])
# TODO: this keeps wrapping values in {}
def create(model_name):
    model = get_model_from_string(model_name)
    instance = model(**request.form)
    db.session.add(instance)
    db.session.commit()
    return "success\n"

# curl localhost:5000/clients/1/edit
@app.route('/<string:model_name>/<int:model_id>/edit', methods=['GET'])
def edit(model_name, model_id):
    return 'render edit form for ' + model_name + ' (' + str(model_id) + ')\n'

# curl --data "name=updated_name" localhost:5000/clients/1
@app.route('/<string:model_name>/<int:model_id>', methods=['POST', 'PUT'])
def update(model_name, model_id):
    model = get_model_from_string(model_name)
    instance = model.query.filter(model.id == model_id)
    instance.update(request.form)
    db.session.commit()
    return "success\n"


# curl -x "DELETE" localhost:5000/clients/1
@app.route('/<string:model_name>/<int:model_id>', methods=['DELETE'])
def destroy(model_name, model_id):
    model = get_model_from_string(model_name)
    instance = model.query.filter(model.id == model_id)
    instance.delete()
    db.session.commit()
    return "success\n"





