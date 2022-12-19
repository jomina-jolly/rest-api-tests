import pytest
import logging as logger
from src.utilites.genericUtilities import generate_random_email_and_password

pytest.mark.tcid29
def test_create_customer_email_passowrd_only():

    logger.info("TEST: Create customer with email and password only")

    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password  = rand_info['password']

    logger.info("Email and password: {},{}".format(email,password))
    #create payload

    #make the call

    #verify status call

    #verify email id in response

    #verify in DB

