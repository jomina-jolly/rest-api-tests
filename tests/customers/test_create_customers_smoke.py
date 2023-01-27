import pytest
import logging as logger
from src.utilites.genericUtilities import generate_random_email_and_password
from src.helpers.customers_helper import CustomerHelper
from src.dao.customers_dao import CustomerDAO
from src.utilites.requestUtilities import RequestsUtilites

@pytest.mark.customers
@pytest.mark.smoke
@pytest.mark.tcid1
def test_create_customer_email_passowrd_only():

    logger.info("TEST: Create customer with email and password only")

    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password  = rand_info['password']
    logger.info("Email and password: {},{}".format(email, password))
    
    #create payload
    payload = {'email': email, 'password':password}

    #make the call
    #Creates the payload
    customer_obj = CustomerHelper()
    customer_api_info = customer_obj.create_customer(email=email, password=password)

    #verify email id in response
    assert customer_api_info['email'] == email, "Customer API returned wrong email id"
    
    #verify in DB
    dao_helper = CustomerDAO()
    resp_dic = dao_helper.get_customer_by_email(email)

    #Check if the IDs are same
    id_api_resp = customer_api_info['id']
    id_db_resp = resp_dic[0]['ID']

    assert id_api_resp == id_db_resp, f"IDs in the API and DB are different \n \
        Email : {email}"


@pytest.mark.customers
@pytest.mark.tcid3
def test_create_customer_fail_existing_email():
    #Get exisiting email id from DB

    dao_helper = CustomerDAO()
    list_of_users = dao_helper.get_random_customer(1)
    email = list_of_users[0]['user_email']

    #Set a random password
    password = "Qwerty@1234"

    #Create user with the email obtained
    request_helper = RequestsUtilites()

    payload = {}
    payload['email'] = email
    payload['password'] = password
    customer_api_info = request_helper.post(endpoint="/wp-json/wc/v3/customers", payload=payload, expected_status_code=400)

    expected_err_code = "registration-error-email-exists"

    #Check for the error message
    assert customer_api_info['code'] == expected_err_code, f"Error code is not as expected. \
        Expected: {expected_err_code}"
