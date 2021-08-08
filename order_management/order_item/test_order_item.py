import unittest

from order_management.order.order import Order
from order_management.order_item.order_item import OrderItem
from order_management.catalogue.catalogue import CATALOGUE

class Test_OrderItem(unittest.TestCase):
    
    def test_order_item_amount(self):
        order = Order()
        order_id = order.order_id

        item = 'Pen'
        qty = 250

        oi = OrderItem(order_id, item, qty)

        self.assertEqual(oi.amount, qty*CATALOGUE[item])
        