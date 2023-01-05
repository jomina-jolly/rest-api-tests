import pytest
import logging as logger
# from src.utilites.genericUtilities import generate_random_email_and_password
from src.utilites.requestUtilities import RequestsUtilites
from src.dao.customers_dao import CustomerDAO


@pytest.mark.tcid2
def test_get_customers():

    #Call get customers API
    request_helper = RequestsUtilites()

    endpoint = "/wp-json/wc/v3/customers"
    api_resp = request_helper.get(endpoint=endpoint)

    #Check if the response size is not empty
    assert api_resp, f"List of customers is empty"
