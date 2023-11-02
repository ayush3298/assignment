from behave import given, when, then
from APIcomparatorlib import APIComparator 


@given('I have API request URLs from "{file1}" and "{file2}"')
def step_impl(context, file1, file2):
    context.api_comparator = APIComparator(file1, file2)
    

@when('I compare the API responses')
def step_impl(context):
    context.api_comparator.compare_responses()

@then('the responses should be equal')
def step_impl(context):
    context.api_comparator.are_responses_equal()

@then('the responses should not be equal')
def step_impl(context):
   not context.api_comparator.are_responses_equal()
