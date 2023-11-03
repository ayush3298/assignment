from behave import given, when, then
from APIcomparatorlib import APIComparator 
import multiprocessing
num_threads = multiprocessing.cpu_count() 


@given('I have API request URLs from "{file1}" and "{file2}"')
def api_req_from_files(context, file1, file2):
    context.api_comparator = APIComparator(file1, file2)
    

@when('I compare the API responses')
def compare_response(context):
    context.api_comparator.compare_responses(num_threads)

@then('the responses should be equal')
def response_equal(context):
    response = context.api_comparator.are_responses_equal()
    assert response == False, "the response are equal for both API"

@then('the responses should not be equal')
def response_not_equal(context):
   response = not context.api_comparator.are_responses_equal()
   assert response == True, "the response are not equal for both API"

