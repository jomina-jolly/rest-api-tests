import logging as logger
import random
import string

def generate_random_email_and_password(domain=None, prefix=None):

    #Email
    if not domain:
        domain = "xyz.com"
    if not prefix:
        prefix = "testuser"

    email_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=email_length))
    email_id = prefix + random_string + "@" + domain

    #password
    password_length = 10
    password = "".join(random.choices(string.ascii_letters, k=password_length))

    random_info = {'email':email_id, 'password':password}
    logger.info("Email and password is {}, {}".format(email_id,password))
    print (random_info)
    return random_info

