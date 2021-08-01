import unittest

from order_management.order.order import Order

class Test_Order_Creation(unittest.TestCase):
    def test_order_creation_1(self):
        order1 = Order()
        self.assertEqual(order1.order_id, 0)

        order2 = Order()
        self.assertEqual(order2.order_id, 1)


if __name__ == '__main__':
    unittest.main()
