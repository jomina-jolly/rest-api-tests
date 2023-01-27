from src.utilites.dbUtilities import DBUtilities
import random

class ProdcutDAO():

    def __init__(self) -> None:
        self.db_helper = DBUtilities()

    def get_product_by_id(self, id):
        sql = f"SELECT * FROM marketplace.wp_posts WHERE post_type='product' and ID={id} ;"
        resp_dic = self.db_helper.execute_select(sql=sql)
        return resp_dic

    def get_random_product(self, qty=1):
        sql = f"SELECT * FROM marketplace.wp_posts WHERE post_type='product' ORDER BY ID DESC LIMIT 500;"
        prd_list_db_rsp = self.db_helper.execute_select(sql=sql)
        return random.sample(prd_list_db_rsp, qty)

    def get_list_of_products_after_date(self, date):
        sql = f"SELECT * FROM marketplace.wp_posts WHERE post_type='product' AND post_date > '{date}';"
        prd_list_db_rs = self.db_helper.execute_select(sql=sql)
        return prd_list_db_rs

    