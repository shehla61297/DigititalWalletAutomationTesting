import requests
from automation.tests.conftest import Config
import json
import logging


logging.getLogger().setLevel(logging.INFO)
log = logging.getLogger("Log")

endpointUrl = None
responseBody = None


def get_endpoint_for_service():
    log.info("START:get_endpoint_for_Digital Wallet")
    api_url = Config.get_base_url()
    return api_url


def get_endpoint_for_users_with_id():
    log.info("START:get_endpoint_for_user_with_id")
    base = Config.get_base_url()
    endpoint = Config.get_api_endpoint()
    api_url = base + endpoint
    log.info(api_url)
    log.info("END:get_endpoint_for_user_with_id")
    return api_url


def request_get_user_list_api(endpoint):
    log.info("START:request_get_user_list_Digital Wallet")
    response = None
    try:
        session = requests.Session()
        response = session.get(url=endpoint)
    except Exception as e:
        log.error(e)
    finally:
        assert response is not None
    #log.info("END:request_get_digital Wallet")
    return response


def get_id_appended_at_endpoint(endpoint, userid):
    log.info("START:get_id_append_at_endpoint")
    log.info(endpoint.format(userid))
    log.info("END:get_id_appended_at_endpoint")
    return endpoint.format(userid)
