import pytest
import logging as logger
from src.utilites.genericUtilities import generate_random_email_and_password
from src.helpers.customers_helper import CustomerHelper

pytest.mark.tcid29
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
    import pdb; pdb.set_trace()
    
    #verify status call

    #verify email id in response

    #verify in DB

