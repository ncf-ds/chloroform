from flask import request
from flask import jsonify
from flask import Flask, render_template
from chloroform import app
from chloroform.database import db
from chloroform import models

SUCCESS_MESSAGE = "success"


# View helpers
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
    elif isinstance(py_object, db.Model):
        row = py_object
        row = row.__dict__
        row.pop('_sa_instance_state', None)
        return jsonify(row)
    else:
        # TODO: make exceptional
        return "Data not found"







# Normal single purpose routes

@app.route('/')
def index():
    return render_template('index.html')

# curl localhost:5000/form/1/edit
@app.route('/forms/<int:form_id>/edit', methods=['GET'])
def edit_form_load(form_id):
    form = models.Form.query.get(form_id)
    return jsonify(form.jsonify()) # TODO: make all model.jsonify()'s actually return json

@app.route('/<string:model_name>/name/<string:name>')
def search( model_name,name):
    model = get_model_from_string(model_name)
    rows = model.query.filter(model.name.ilike('%{}%'.format(name))).order_by(model.name).all()
    return dump_to_json(rows)






# The following are CRUD endpoints for each table

# curl localhost:5000/clients
@app.route('/<string:model_name>')
def model_index(model_name):
    model = get_model_from_string(model_name)
    rows = model.query.all()
    return dump_to_json(rows)


# curl localhost:5000/clients/1
@app.route('/<string:model_name>/<int:model_id>')
def model_show(model_name, model_id):
    model = get_model_from_string(model_name)
    instance = model.query.get(model_id)
    return dump_to_json(instance)


# curl --data "name=new_client" localhost:5000/clients
@app.route('/<string:model_name>', methods=['POST'])
def model_create(model_name):
    model = get_model_from_string(model_name)
    instance = model(**request.form.to_dict())
    db.session.add(instance)
    db.session.commit()
    return jsonify({"message": SUCCESS_MESSAGE, "id": instance.id})


# curl --data "name=updated_name" localhost:5000/clients/1
@app.route('/<string:model_name>/<int:model_id>', methods=['POST', 'PUT'])
def model_update(model_name, model_id):
    model = get_model_from_string(model_name)
    instance = model.query.filter(model.id == model_id)
    instance.update(request.form)
    db.session.commit()
    return jsonify({"message": SUCCESS_MESSAGE})



# curl -x "DELETE" localhost:5000/clients/1
@app.route('/<string:model_name>/<int:model_id>', methods=['DELETE'])
def model_destroy(model_name, model_id):
    model = get_model_from_string(model_name)
    instance = model.query.filter(model.id == model_id)
    instance.delete()
    db.session.commit()
    return jsonify({"message": SUCCESS_MESSAGE})





