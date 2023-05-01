from behave import given, when, then, step


@given('I have no users')
def step_impl(context):
    context.db.clear()


@given('I have a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.db.add_user(username, password)


@given('I only have the following users')
def step_impl(context):
    context.db.clear()
    for user in context.table:
        context.db.add_user(username=user[0], password=user[1])


@when('I add a new user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.response = context.client.post('/users', json={'username': username, 'password': password})
    assert context.response.status_code == 200
    assert context.db.get_user(username)[0]['password'] == password


@when('I retrieve the user "{username}"')
def step_impl(context, username):
    context.response = context.client.get(f'/user/{username}')
    response_json = context.response.json()
    assert context.response.status_code == 200
    assert len(response_json) == 1


@then('user "{username}" is in the system')
def step_impl(context, username):
    user = context.db.get_user(username)
    assert len(user) == 1


@then('user "{username}" has a password of "{password}"')
def step_impl(context, username, password):
    assert context.db.get_user(username)[0]['password'] == password


@then('the user\'s password is "{password}"')
def step_impl(context, password):
    assert context.response.json()[0].get('password', '') == password


@when("I retrieve all users")
def step_impl(context):
    context.response = context.client.get('/users')
    assert context.response.status_code == 200


@then(u'the retrieved users are')
def step_impl(context):
    expected_users = context.table
    actual_users = {user['username']: user['password'] for user in context.response.json()}
    for user in expected_users:
        assert actual_users.get(user[0]) == user[1]


@step("the user has no password")
def step_impl(context):
    raise NotImplementedError(u'STEP: But the user has no password')
