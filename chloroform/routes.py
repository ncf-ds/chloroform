from flask import Flask
from flask import request
from flask import jsonify
from flask import Flask,render_template
from chloroform import app
from chloroform.database import db
from chloroform import models

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


@app.route('/')
def index():
    return render_template('index.html')


# curl localhost:5000/clients
# curl localhost:5000/clients/1
@app.route('/<string:model_name>/', defaults={'model_id': None})
@app.route('/<string:model_name>/<int:model_id>')
def show(model_name, model_id,title):
    model = get_model_from_string(model_name)
    if (model_id):
        instance = model.query.get(model_id)
        return dump_to_json(instance)
    else:
        rows = model.query.all()
        return dump_to_json(rows)

# curl --data "name=new_client" localhost:5000/clients
@app.route('/<string:model_name>/', methods=['POST'])
def create(model_name):
    model = get_model_from_string(model_name)
    instance = model(**request.json)
    db.session.add(instance)
    db.session.commit()
    return "success\n"

# curl --data "name=updated_name" localhost:5000/clients/1
@app.route('/<string:model_name>/<int:model_id>', methods=['POST', 'PUT'])
def update(model_name, model_id):
    model = get_model_from_string(model_name)
    instance = model.query.filter(model.id == model_id)
    instance.update(request.json)
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


@app.route('/<string:model_name>/name/<string:name>')
def search( model_name,name):
    model = get_model_from_string(model_name)
    rows = model.query.filter(model.name.ilike('%{}%'.format(name))).order_by(model.name).all()
    return dump_to_json(rows)





