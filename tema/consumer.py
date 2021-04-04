"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
import time


class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)

        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time

    def run(self):
        for cart in self.carts:
            c_id = self.marketplace.new_cart()

            for cons_op in cart:
                num_of_ops = 0

                while num_of_ops < cons_op["quantity"]:
                    if cons_op["type"] == "add":
                        ret = self.marketplace.add_to_cart(str(c_id), cons_op["product"])
                    else:
                        ret = self.marketplace.remove_from_cart(str(c_id), cons_op["product"])

                    if ret:
                        num_of_ops += 1
                    else:
                        time.sleep(self.retry_wait_time)

            self.marketplace.place_order(c_id)
