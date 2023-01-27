import requests
from src.configs.hosts_config import API_HOSTS
from src.utilites.credentialUtilities import CredentialUtilites
import os
import json
from requests_oauthlib import OAuth1
import logging as logger

class RequestsUtilites():

    def __init__(self) -> None:
        self.env = os.environ.get('ENV', "test")
        self.base_url = API_HOSTS[self.env] + "/wp-json/wc/v3/"

        api_credentials = CredentialUtilites.get_wc_api_keys()
        API_KEY = api_credentials['wc_key']
        API_SECRET = api_credentials['wc_secret']
        self.auth = OAuth1(API_KEY, API_SECRET)

    def assert_status_code(self):
        assert self.expected_status_code == self.status_code, \
            f"Expected status code {self.expected_status_code} but got {self.status_code} \n\
            for the URL {self.url} \n \
            respose json: {self.rs_json}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        
        self.expected_status_code = expected_status_code
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint

        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.rs_json = rs_api.json()

        #Check the status code
        self.assert_status_code()

        logger.debug(f'POST API response {self.rs_json}')
        return self.rs_json
        
    def get(self, endpoint, params=None, headers=None, expected_status_code=200):
        
        self.expected_status_code = expected_status_code

        if not headers:
            headers = {"Content-Type": "application/json"}
        
        self.url = self.base_url + endpoint

        rs_api = requests.get(url=self.url, data=json.dumps(params), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code

        self.rs_json = rs_api.json()
        #Check the status code
        self.assert_status_code()
        logger.debug(f'GET API response {self.rs_json}')
        
        return self.rs_json
