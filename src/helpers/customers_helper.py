from src.utilites.genericUtilities import generate_random_email_and_password
from src.utilites.requestUtilities import RequestsUtilites

class CustomerHelper():

    def __init__(self) -> None:
        self.request_utility = RequestsUtilites()

    def create_customer(self, email=None, password=None, **kwarg):

        if not email:
            rand_info = generate_random_email_and_password()
            email = rand_info['email']
        if not password:
            password = "Qwerty@123"

        payload = {}
        payload['email'] = email
        payload['password'] = password
        payload.update(kwarg)

        create_customers_resp = self.request_utility.post(endpoint="/wp-json/wc/v3/customers", payload=payload, expected_status_code=201)
        return create_customers_resp

