import requests
import json
import logging
import jsonpath
from automation.generic_methods_util import impl_generic
from pytest_bdd import given, when, then, parsers, scenario

logging.getLogger().setLevel(logging.INFO)
log = logging.getLogger("Log")


@scenario('../features/dummyapi.feature', 'Get list of all users')
def test_one():
    pass


@given('application requires a list of users')
def get_service_endpoint():
    log.info("First Test Case to get List of Users")
    impl_generic.endpointUrl = impl_generic.get_endpoint_for_service()
    log.info(impl_generic.endpointUrl)
    assert impl_generic.endpointUrl == "https://reqres.in/api/users"


@when('get request is sent to the endpoint')
def get_request():
    impl_generic.responseBody = impl_generic.request_get_user_list_api(impl_generic.endpointUrl)


@then(parsers.parse('list of users is returned as a Json response with the HTTP status "{code:d}"'))
def verify_response():
    assert impl_generic.responseBody.status_code == 200
    data = impl_generic.responseBody.json()
    if bool(data) is True:
        log.info(data)
        # print("Data is there ", data)
        json_response = json.loads(impl_generic.responseBody.text)
        total_users = jsonpath.jsonpath(json_response, 'total')
        print(impl_generic.responseBody.content)
        assert total_users[0] == 12
    else:
        assert bool(data) is False
    log.info("END:verify_response")





