import unittest

from order_management.order.order import Order
from order_management.order_item.order_item import OrderItem

class Test_OrderItem(unittest.TestCase):
    def test_order_item_creation(self):
        order = Order()
        order_id = order.order_id

        item = 'Book'
        qty = 20

        oi = OrderItem(order_id, item, qty)
        
        self.assertEqual(oi.order_item_id, 0)
    
    def test_unknown_item_creation(self):
        order = Order()
        order_id = order.order_id

        item = 'Pen'
        qty = 100

        oi = OrderItem(order_id, item, qty)
        print(oi)
        self.assertEqual(oi.order_item_id, 1)
        