import logging as logger
from src.utilites.requestUtilities import RequestsUtilites
from src.helpers.product_helpers import ProductHelpers
from src.dao.product_dao import ProdcutDAO
import pytest

product_helper = ProductHelpers()
pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.tcid5
def test_get_products():
    #Get all products and check for a not empty list

    #Call the API
    request_helper = RequestsUtilites()

    api_product_list = product_helper.call_list_products()
    api_number_of_products = len(api_product_list)
    
    assert api_number_of_products, "Product list returned None"

@pytest.mark.tcid4
def test_retrieve_product_by_id():
    
    #Get product from DB
    db_product_helper = ProdcutDAO()
    prd_detail_frm_db = db_product_helper.get_random_product(1)

    db_prd_id = prd_detail_frm_db[0]['ID']
    db_prd_name = prd_detail_frm_db[0]['post_title']

    #Call API
    api_info_prd = product_helper.get_product_by_id(db_prd_id)
    api_prd_name = api_info_prd['name']
    
    logger.info(f'DB product details: {prd_detail_frm_db}\n API product details: {api_info_prd}')
    assert db_prd_name == api_prd_name , "Product names doesn't match"

