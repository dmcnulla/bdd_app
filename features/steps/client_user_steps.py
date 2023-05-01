from behave import given, when, then


@given('I have no users')
def step_impl(context):
    context.db.clear()


@when('I add a new user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.response = context.client.post('/users', json={'username': username, 'password': password})
    assert context.response.status_code == 200
    assert context.db.get_user(username)[0]['password'] == password


@then('user "{username}" is in the system')
def step_impl(context, username):
    user = context.db.get_user(username)
    assert len(user) == 1


@then('user "{username}" has a password of "{password}"')
def step_impl(context, username, password):
    assert context.db.get_user(username)[0]['password'] == password
