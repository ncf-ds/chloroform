import os
import sys

# adding root of project to sys path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from chloroform.views import app, SUCCESS_MESSAGE
import json

curl = app.test_client()

RANDOM_TEXT = ["fake text", "more fake text"]

def load_response(response, check_success = False):
    loaded_response = json.loads(response.data.decode())
    if check_success:
        assert loaded_response['message'] == SUCCESS_MESSAGE
    return loaded_response

def test_route(url, data):
    return load_response(curl.post(url, data=json.dumps(data), content_type='application/json'), check_success=True)


def test_crud(route, initial_data, field_to_update):
    create_response = test_route(route, initial_data)
    id_string = str(create_response['id'])
    get_response = load_response(curl.get(route + '/' + id_string))
    for key in initial_data:
        assert get_response[key] == initial_data[key]

    test_route(route + '/' + id_string, {field_to_update: RANDOM_TEXT[1]})
    get_response = load_response(curl.get(route + '/' + id_string))
    assert get_response[field_to_update] == RANDOM_TEXT[1]
    load_response(curl.delete(route + '/' + id_string), check_success=True)


# Choice
test_crud('/choices', {'text': RANDOM_TEXT[0]}, 'text')

# ChoiceTemplate
test_crud('/choice_templates', {'template': RANDOM_TEXT[0]}, 'template')

# Form
test_crud('/forms', {'title': RANDOM_TEXT[0]}, 'title')

# Madlibs
test_crud('/madlibs', {
    # "placeholder": RANDOM_TEXT[0], 
    # "word_type": RANDOM_TEXT[0], 
    "word": RANDOM_TEXT[0]
}, 'word')

# Questions
test_crud('/questions', {
    # "question_type": RANDOM_TEXT[0], 
    "text": RANDOM_TEXT[0]
}, 'text')

# Retail Chains
test_crud('/form_contexts', {"name": RANDOM_TEXT[0]}, 'name')


# QuestionGroups

# QuestionGroupTemplates

# QuestionTemplates


