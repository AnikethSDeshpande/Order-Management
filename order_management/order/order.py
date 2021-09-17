'''
    Author: Aniketh Deshpande

    Order Class
        - Maintains order related information
    
    Fields
        - Customer
        - GST Number
        - Order Items
        - Order Value
        - Tax
        - Delivery Status
'''

import logging

from order_management.config import GST_NUMBER_LENGHT
from order_management.order_item.order_item import OrderItem
import re

class Order:
    _order_ids = [0]

    def __init__(self, customer=None):
        self.order_id = self.get_last_order_id()
        Order._order_ids.append(self.order_id + 1)
        self.order_items = []
        self.customer = customer
    
    @classmethod
    def get_last_order_id(cls):
        return Order._order_ids[-1]

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        try:
            if not isinstance(customer, str):
                if customer == None:
                    self._customer = customer
                else:
                    raise Exception('invalied customer name')
            self._customer = customer
        
        except Exception as e:
            logging.ERROR('error while setting customer: {e}')

    @property
    def gst_number(self):
        return self._gst_number
    
    @gst_number.setter
    def gst_number(self, gst_number):
        try:
            if not isinstance(gst_number, str):
                raise Exception('gst_not_string')
            if not len(gst_number) == GST_NUMBER_LENGHT:
                raise Exception('gst_len_error')
            self._gst_number = gst_number
        except Exception as e:
            logging.ERROR('error while setting gst_number: {e}')
    

    @property
    def order_total(self):
        '''
            calculates the total value of order based on the items added to the order
        '''
        order_total = 0
        for order_item in self.order_items:
            order_total += order_item.amount

        return order_total


    def add_item(self, item_name=None, qty=None, rate=None):
        '''
            add item to the list of items in the order
        '''
        item = OrderItem(order_id=self.order_id,
                         item_name=item_name,
                         qty=qty
                        )
        self.order_items.append(item)
    
    def __repr__(self) -> str:
        repr = f'order_id: {self.order_id}, customer: {self.customer}'
        return repr

    def print_order(self):
        order_string = str()
        order_id = self.order_id
        customer = self.customer
        gst_number = self.gst_number
        order_total = self.order_total
        
        order_string += f'Order ID: {order_id}\n'
        order_string += f'Customer: {customer}\n'
        order_string += f'GST Number: {gst_number}\n\n'

        order_string += 'Items'

        items = [item for item in self.order_items]
        
        for i, item in enumerate(items):
            order_string += f'\n{i+1}--------------------------------------\n{item}'
        
        order_string += '\n---------------------------------------'
        order_string += f'\n Total: {order_total}'
        # comment!
        return order_string
