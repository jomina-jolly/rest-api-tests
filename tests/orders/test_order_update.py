import pytest
from src.helpers.orders_helper import OrderHelper
from src.utilites.woocommerce_api_utility import WooCommerceAPI

pytestmark = [pytest.mark.orders]


@pytest.mark.parametrize("new_status", 
                        [
                            pytest.param("cancelled", marks=pytest.mark.tcid10),
                            pytest.param("refunded", marks=pytest.mark.tcid11),
                            pytest.param("completed", marks=pytest.mark.tcid12)
                            ])
def test_update_order_status(new_status):

    new_status = "cancelled"

    #Create order
    order_helper = OrderHelper()
    woocommerce_api = WooCommerceAPI()

    order_details = order_helper.create_order()
    order_id = order_details['id']

    #Call the API to udpate the status
    endpoint = f"orders/{order_id}"
    payload = {"status": new_status}
    rs_api_json = woocommerce_api.put(endpoint=endpoint, params=payload)
    
    #Get udpated status from API
    rs_api_udpated_status = rs_api_json['status']
    assert rs_api_udpated_status==new_status, f'The order status is not udpated \n \
        Expected:{new_status}, Result: {rs_api_udpated_status}'

    #Retrieve the order details with API and check the status
    updated_order_details = order_helper.call_retrieve_order_details(order_id=order_id)
    current_order_status = updated_order_details['status']
    assert current_order_status == new_status, f'Status is not updated correctly\n \
        Expected: {new_status}, Result: {current_order_status}'
