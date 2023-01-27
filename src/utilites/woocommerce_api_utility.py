import logging as logger
from src.configs.hosts_config import API_HOSTS
from src.utilites.credentialUtilities import CredentialUtilites
import os
from woocommerce import API


class WooCommerceAPI():
    '''
    The python module provided by the creator to call the API.
    '''

    def __init__(self) -> None:

        self.env = os.environ.get('ENV', "test")
        self.base_url = API_HOSTS[self.env]

        api_credentials = CredentialUtilites.get_wc_api_keys()
        API_KEY = api_credentials['wc_key']
        API_SECRET = api_credentials['wc_secret']

        self.wcapi = API(
            url=self.base_url,
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            version="wc/v3"
            )

    def assert_status_code(self):
        '''
        Verifies the status code for all the API calls made
        '''
        assert self.expected_status_code == self.status_code, \
            f"Expected status code {self.expected_status_code} but got {self.status_code} \n\
            for the URL {self.url} \n \
            respose json: {self.rs_json}"

    def get(self, endpoint, params=None, expected_status_code=200):
        self.expected_status_code = expected_status_code

        rs_api = self.wcapi.get(endpoint, params=params)
        self.status_code = rs_api.status_code
        rs_api_json = rs_api.json()

        #Assert the status code
        self.assert_status_code()

        return rs_api_json

    def post(self, endpoint, params=None, expected_status_code=200):
        self.expected_status_code = expected_status_code

        rs_api = self.wcapi.post(endpoint, data=params)
        self.status_code = rs_api.status_code
        rs_api_json = rs_api.json()

        #Assert the status code
        self.assert_status_code()

        return rs_api_json