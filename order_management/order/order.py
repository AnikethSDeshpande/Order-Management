import logging

class Order:
    _order_ids = [0]

    def __init__(self):
        self.order_id = self.get_last_order_id()
        Order._order_ids.append(self.order_id + 1)
        print('@@@@@setting order id: ', self.order_id)
        # logging.INFO('setting order id: ', self.order_id)
    
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
            if not len(gst_number) == 3:
                raise Exception('gst_len_error')
            self._gst_number = gst_number
        except Exception as e:
            logging.ERROR('error while setting gst_number: {e}')

