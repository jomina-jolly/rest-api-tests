import pytest
import logging as logger
# from src.utilites.genericUtilities import generate_random_email_and_password
from src.utilites.requestUtilities import RequestsUtilites
from src.dao.customers_dao import CustomerDAO


@pytest.mark.tcid2
def test_get_customers():
    #Just checking if the response is empty of not. Depending on the size of the application, you may add new checks for testing the API\
    #eg, check with pagination (which is not included here)

    #Call get customers API
    request_helper = RequestsUtilites()

    endpoint = "customers"
    api_resp = request_helper.get(endpoint=endpoint)

    #Check if the response size is not empty
    assert api_resp, f"List of customers is empty"
