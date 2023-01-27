import pytest
from src.dao.product_dao import ProdcutDAO
from src.helpers.orders_helper import OrderHelper
from src.dao.order_dao import OrderDao
from src.helpers.customers_helper import CustomerHelper

pytestmark = [pytest.mark.order]

@pytest.fixture(scope='module')
def orders_test_setup():
    product_dao = ProdcutDAO()
    num_prd_to_add = 2
    rand_prds = product_dao.get_random_product(qty=num_prd_to_add)
    product_ids = [product['ID'] for product in rand_prds]
    return {
        'product_ids':product_ids,
        }

@pytest.mark.tcid8
def test_create_paid_order__guest_user(orders_test_setup):
    '''
    Test order creation with guest user
    Payload template and default values pulled from a file
    Product details are upadted in the code. 
    '''

    order_helper = OrderHelper()
    #payload
    #get a random product from DB to create order
    num_prd_to_add = 2
    
    product_ids = orders_test_setup['product_ids']
    customer_id = 0
    payload_line_item = {'line_items':[]}
    for product_id in product_ids:
        line_item = {
            "product_id": product_id,
            "quantity": 1
             }
        payload_line_item['line_items'].append(line_item)

    #Call the order API
    additional_items = {}
    additional_items.update(payload_line_item)

    
    rs_order_json = order_helper.create_order(additional_args=additional_items)
    order_helper.verify_order_is_created(rs_order_json, customer_id, product_ids)


@pytest.mark.tcid9
def test_create_order_with_new_user(orders_test_setup):
    order_helper = OrderHelper()
    customer_helper = CustomerHelper()

    #payload
    #Random products
    product_ids = orders_test_setup['product_ids']

    #Create customer
    customer_details = customer_helper.create_customer()
    customer_id = customer_details['id']

    payload_line_item = {'line_items':[]}
    for product_id in product_ids:
        line_item = {
            "product_id": product_id,
            "quantity": 1
             }
        payload_line_item['line_items'].append(line_item)

    #Call the order API
    additional_items = {}
    additional_items.update(payload_line_item)

    rs_order_json = order_helper.create_order(additional_args=additional_items)
    order_helper.verify_order_is_created(rs_order_json, customer_id, product_ids)