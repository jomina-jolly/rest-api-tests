from src.utilites.dbUtilities import DBUtilities

class CustomerDAO():

    def __init__(self) -> None:
        self.db_helper = DBUtilities()


    def get_customer_by_email(self, email):

        sql = f"SELECT * FROM marketplace.wp_users WHERE user_email = '{email}';"
        resp_dic = self.db_helper.execute_select(sql=sql)
        return resp_dic