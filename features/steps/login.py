from behave import *


@given(u'I navigated to Login page')
def step_impl(context):
    pass


@when(u'I enter valid email address as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    pass


@when(u'I click on Login button')
def step_impl(context):
    pass


@then(u'I should get logged in')
def step_impl(context):
    pass


@when(u'I enter invalid email address as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    pass


@then(u'I should get a proper warning message')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should get a proper warning message')


@when(u'I enter valid email address as "{email}" and invalid password as "{password}" into the fields')
def step_impl(context, email, password):
    pass


@when(u'I enter invalid email address as "{email}" and invalid password as "{email}" into the fields')
def step_impl(context, email, password):
    pass


@when(u'I do not enter anything into email address and password fields')
def step_impl(context):
    pass
