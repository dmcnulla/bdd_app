from behave import when, then


@when('I call the greet endpoint')
def step_impl(context):
    context.response = context.client.get('/')


@then('I should get a greeting')
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.json() == {'message': 'Hello, world'}
