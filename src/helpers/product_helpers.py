from src.utilites.requestUtilities import RequestsUtilites

class ProductHelpers():

    def __init__(self) -> None:
        self.request_utility = RequestsUtilites()

    def get_product_by_id(self, id):
        end_point = f"products/{id}"
        prd_info = self.request_utility.get(endpoint=end_point)
        return prd_info

    def create_product(self, payload):
        end_point = "products"
        create_prd_rs = self.request_utility.post(endpoint=end_point, payload=payload, expected_status_code=201)
        return create_prd_rs

    def call_list_products(self, payload=None): 
        '''
        #The api has pagination, https://woocommerce.github.io/woocommerce-rest-api-docs/?python#list-all-products
        '''
        end_point = "products"

        if not payload['per_page']:
            items_per_page = 100
        else:
            items_per_page = payload['per_page']
            
        #Repeat the call till the end of the products.
        prds_list = []
        page_num = 1
        last_page = False
        while not last_page:
            list_prds_per_page = self.request_utility.get(endpoint=end_point, params=payload)
            prds_list += list_prds_per_page
            page_num +=1 #Increment the page number after each call
            if len(list_prds_per_page) < items_per_page:
                last_page = True
        return prds_list