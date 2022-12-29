import requests
from src.configs.hosts_config import API_HOSTS, API_KEYS
import os
import json
from requests_oauthlib import OAuth1
import logging as logger

class RequestsUtilites():

    def __init__(self) -> None:
        self.env = os.environ.get('ENV', "test")
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1("ck_2f470547a4ab1feefadf26049469580bb2f518af", "cs_0d21cad3a14073214a373047cbef8696bf172591")
        # import pdb; pdb.set_trace()

    def assert_status_code(self):
        assert self.expected_status_code == self.assert_status_code, \
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

        logger.debug[f'Customer API response {self.rs_json}']
        return self.rs_json
        
    def get(self):
        pass