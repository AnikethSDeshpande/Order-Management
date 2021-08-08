import unittest

from order_management.order.order import Order
from order_management import CATALOGUE

class Test_Order_Creation(unittest.TestCase):
    def test_order_creation_1(self):
        order1 = Order()
        self.assertEqual(order1.order_id, 0)

        order2 = Order()
        self.assertEqual(order2.order_id, 1)
    
    def test_set_customer(self):
        order = Order()
        order.customer = 'Aniketh'
        self.assertEqual(order.customer, 'Aniketh')
    
    def test_set_gst_number(self):
        order = Order()
        order.gst_number = '123'
        self.assertEqual(order.gst_number, '123')
    
    def test_order_item_addition(self):
        order = Order()
        order.customer = 'Aniketh'
        order.gst_number = '123'

        item_name = 'Pen'
        qty = 100
        order.add_item(item_name, qty)

        self.assertEqual(order.order_total, qty*CATALOGUE[item_name])


if __name__ == '__main__':
    unittest.main()
