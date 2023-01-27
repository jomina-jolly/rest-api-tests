from src.utilites.dbUtilities import DBUtilities

class OrderDao():
    '''
    All the frequent DB queries on order
    '''

    def __init__(self) -> None:
        self.db_helper = DBUtilities()

    def get_order_line_items_with_order_id(self, id):
        sql = f'SELECT * FROM marketplace.wp_woocommerce_order_items WHERE order_id={id} AND order_item_type="line_item";'
        order_details = self.db_helper.execute_select(sql=sql)
        return order_details

    def get_order_item_details(self, order_item_ids): #order_item_id as an array
        product_ids = []
        for order_item_id in order_item_ids:
            sql = f'SELECT * FROM marketplace.wp_woocommerce_order_itemmeta WHERE order_item_id = {order_item_id}'
            meta_details = self.db_helper.execute_select(sql=sql)
            '''
            The result is expected to have multiple rows each with order item and its value
            Get the result to a dic to access the values
            '''
            product_ids += [meta_item['meta_value'] for meta_item in meta_details if meta_item['meta_key']=='_product_id']
        
        return product_ids

    