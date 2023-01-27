import logging as logger
from src.utilites.genericUtilities import generate_generic_name
from src.helpers.product_helpers import ProductHelpers
import pytest



@pytest.mark.products
@pytest.mark.tcid6
def test_create_1_product():
    #details of the API : https://woocommerce.github.io/woocommerce-rest-api-docs/?python#create-a-product
    
    #Generte data
    product_name = generate_generic_name(length=6)
    regular_price = "21.99"
    payload = {
        "name" : product_name,
        "regular_price" : regular_price
    }
    #Call api to create
    product_api = ProductHelpers()
    create_prd_rs = product_api.create_product(payload=payload)
    api_rs_price = create_prd_rs['price']
    api_rs_name = create_prd_rs['name']
    api_rs_id = create_prd_rs['id']

    #check the response for name, and price
    assert api_rs_name == product_name, f"Error in the name of the product, \n Expected name: {product_name}, response has: {api_rs_name}"
    assert api_rs_price == regular_price, f"Error in the name of the price, \n Expected name {regular_price}, Response has: {api_rs_price}"
    '''TODO Neccessary checks to be added depending on the product'''

    #check db for the product with id and validate the name
    product_db_helper = ProductHelpers()
    prd_db_detail = product_db_helper.get_product_by_id(api_rs_id)
    db_product_name = prd_db_detail['name']
    import pdb; pdb.set_trace()
    #Assert the name and price
    assert db_product_name == product_name, f"Name is the DB not matching. Expected {product_name}, Uploaded in DB as {db_product_name} for the ID {api_rs_id}"
