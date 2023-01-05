from src.utilites.dbUtilities import DBUtilities
import random

class CustomerDAO():

    def __init__(self) -> None:
        self.db_helper = DBUtilities()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM marketplace.wp_users WHERE user_email = '{email}';"
        resp_dic = self.db_helper.execute_select(sql=sql)
        return resp_dic

    def get_random_customer(self, qty=1):
        sql = f"SELECT * FROM marketplace.wp_users ORDER BY ID DESC LIMIT 500;"
        customer_list_db_rsp = self.db_helper.execute_select(sql=sql)
        return random.sample(customer_list_db_rsp, qty)