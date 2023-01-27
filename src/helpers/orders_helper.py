import os
import json
from src.utilites.woocommerce_api_utility import WooCommerceAPI
from src.dao.order_dao import OrderDao

class OrderHelper():
    def __init__(self) -> None:
        #get the file path 
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.woo_helper = WooCommerceAPI()

    def create_order(self, additional_args=None): #Expects the additional_args to be dict
        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'create_order_payload.json')

        with open(payload_template) as payload_file:
            payload = json.load(payload_file)

        if additional_args:
            payload.update(additional_args)

        rs_api = self.woo_helper.post('orders', params=payload, expected_status_code=201)
        return rs_api
    
    def verify_order_is_created(self, create_order_json, expected_custumer_id, expected_product_ids):
        order_dao = OrderDao()

        order_id = create_order_json['id']
        rs_api_customer_id = create_order_json['customer_id']
        rs_api_product_ids = [line_item['product_id'] for line_item in create_order_json['line_items']]

        #verify resp
        assert create_order_json, f"Order json after order create is empty"
        # Verify the product ids
        assert set(expected_product_ids) == set(rs_api_product_ids), f"The product list in the API response is not correct\
            Expected: {expected_product_ids}, Response: {rs_api_product_ids}"
        #Customer id should be 0 for guest user
        assert rs_api_customer_id==0, f"Customer id not 0"

        #check db
        db_order_details = order_dao.get_order_line_items_with_order_id(order_id)
        assert db_order_details, f"Order not created in the db"

        #The order item id corresponding to products
        db_order_item_ids = [db_order_items['order_item_id'] for db_order_items in db_order_details]

        #Get the list of product ids
        _db_product_ids = order_dao.get_order_item_details(db_order_item_ids)
        #Convert the ids to int
        db_product_ids = map(int, _db_product_ids)
        assert set(rs_api_product_ids) == set(db_product_ids), f"The product ids in DB differs from the API response \n \
            Expected : {expected_product_ids}, API response: {rs_api_product_ids}, DB response: {db_product_ids}"
