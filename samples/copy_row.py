from flask_sqlalchemy import orm

og_form = Form.query.get(1)

# db.session.expunge(og_form)  # expunge the object from session
orm.session.make_transient(og_form)  # http://docs.sqlalchemy.org/en/rel_1_1/orm/session_api.html#sqlalchemy.orm.session.make_transient

og_form.id = None
db.session.add(og_form)