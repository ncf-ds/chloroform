from app.routes import app
import json

curl = app.test_client()

SUCCESS_MESSAGE = "success"
RANDOM_TEXT = ["fake text", "more fake text"]

def load_response(response, check_success = False):
    loaded_response = json.loads(response.data.decode())
    if check_success:
        assert loaded_response['message'] == SUCCESS_MESSAGE
    return loaded_response

# Choice
post_response = load_response(curl.post('/choices', data={"text": RANDOM_TEXT[0]}), check_success=True)
get_response = load_response(curl.get('/choices/' + str(post_response['id'])))
assert get_response['text'] == RANDOM_TEXT[0]

load_response(curl.post('/choices/' + str(post_response['id']), data={"text": RANDOM_TEXT[1]}), check_success=True)
get_response = load_response(curl.get('/choices/' + str(post_response['id'])))
assert get_response['text'] == RANDOM_TEXT[1]
load_response(curl.delete('/choices/' + str(post_response['id'])), check_success=True)


# ChoiceTemplate
post_response = load_response(curl.post('/choice_templates', data={"template": RANDOM_TEXT[0]}), check_success=True)
get_response = load_response(curl.get('/choice_templates/' + str(post_response['id'])))
assert get_response['template'] == RANDOM_TEXT[0]

load_response(curl.post('/choice_templates/' + str(post_response['id']), data={"template": RANDOM_TEXT[1]}), check_success=True)
get_response = load_response(curl.get('/choice_templates/' + str(post_response['id'])))
assert get_response['template'] == RANDOM_TEXT[1]
load_response(curl.delete('/choice_templates/' + str(post_response['id'])), check_success=True)


# Client
post_response = load_response(curl.post('/clients', data={"name": RANDOM_TEXT[0]}), check_success=True)
get_response = load_response(curl.get('/clients/' + str(post_response['id'])))
assert get_response['name'] == RANDOM_TEXT[0]

load_response(curl.post('/clients/' + str(post_response['id']), data={"name": RANDOM_TEXT[1]}), check_success=True)
get_response = load_response(curl.get('/clients/' + str(post_response['id'])))
assert get_response['name'] == RANDOM_TEXT[1]
load_response(curl.delete('/clients/' + str(post_response['id'])), check_success=True)


# Form
post_response = load_response(curl.post('/forms', data={"title": RANDOM_TEXT[0]}), check_success=True)
get_response = load_response(curl.get('/forms/' + str(post_response['id'])))
assert get_response['title'] == RANDOM_TEXT[0]

load_response(curl.post('/forms/' + str(post_response['id']), data={"title": RANDOM_TEXT[1]}), check_success=True)
get_response = load_response(curl.get('/forms/' + str(post_response['id'])))
assert get_response['title'] == RANDOM_TEXT[1]
load_response(curl.delete('/forms/' + str(post_response['id'])), check_success=True)



# curl.get('/madlibs')

# curl.get('/question_groups')

# curl.get('/question_group_templates')

# curl.get('/questions')

# curl.get('/question_templates')

# curl.get('/retail_chains')
