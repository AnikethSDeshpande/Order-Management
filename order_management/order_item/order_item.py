'''
    Author: Aniketh Deshpande

    Order Item
        - Maintains information regarding the order items

    Fields
        - Item Name
        - Qty
        - Rate
        - Amount
'''

import logging

from order_management.catalogue.catalogue import CATALOGUE


class OrderItem:
    _order_item_ids = [0]

    def __init__(self, order_id, item_name, qty):
        self.order_id = order_id
        self.item_name = item_name
        self.qty = qty

        self.order_item_id = self.get_last_order_item_id()
        OrderItem._order_item_ids.append(self.order_item_id + 1)
    
    @classmethod
    def get_last_order_item_id(cls):
        return OrderItem._order_item_ids[-1]
    
    @property
    def item_name(self):
        return self.item_name_
    
    @item_name.setter
    def item_name(self, item_name):
        try:
            if not item_name in CATALOGUE:
                raise Exception('unknown_item')

            self.item_name_ = item_name
            self.rate = CATALOGUE[item_name]
        except Exception as e:
            logging.ERROR(f'{e}: item not in catalogue')
        


# order_id = 1
# item = 'Book'
# qty = 20

# oi = OrderItem(order_id, item, qty)

# print(oi)
# print(' ')
