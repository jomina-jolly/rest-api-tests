

class CustomerDAO():

    def get_customer_by_email(self, email):

        query = f"SELECT * FROM marketplace.wp_users WHERE user_email = '{email}';"
