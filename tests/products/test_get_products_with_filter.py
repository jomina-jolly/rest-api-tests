import pytest
from datetime import datetime, timedelta
from src.helpers.product_helpers import ProductHelpers
from src.dao.product_dao import ProdcutDAO

@pytest.mark.regression

class TestListProductsWithFilter():

    @pytest.mark.tcid7
    def test_list_products_with_filter_after(self):
        ''' 
        Uses multile filters. 
        Makes use of 'parametrize' in fixtures 
        '''

        #Create test data
        x_days_from_today = 300
        #The time in the filter should be ISO8601 compliant eg: 2017-03-23T17:03:12. YYYY-MM-DDThh:mm:ss (without the microsec, hence the replace() in datetime.now())
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = _after_created_date.isoformat()

        payload = {}
        payload['per_page'] = 10
        payload['after'] = after_created_date
        #make the call
        product_helper = ProductHelpers()
        api_prd_list = product_helper.call_list_products(payload=payload)
        api_no_of_prd = len(api_prd_list)

        #Check the list of products with DB
        product_dao = ProdcutDAO()
        db_prd_list = product_dao.get_list_of_products_after_date(date=after_created_date)
        db_no_of_prd = len(db_prd_list)

        #Check if the no of products is same for API and DB respose
        assert api_no_of_prd == db_no_of_prd, (
            f"Error in number of products in API response \n \
            API list is {api_no_of_prd} where as DB has {db_no_of_prd}")

        api_ids = [i['id'] for i in api_prd_list]
        db_ids = [i['ID'] for i in db_prd_list]

        assert set(api_ids) == set(db_ids), (
            f"The list of products in the API is not same as the DB\
            expected {db_ids}, result obtained {api_ids}")