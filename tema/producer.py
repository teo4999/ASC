"""
This module represents the Producer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""
import time
from threading import Thread


class Producer(Thread):
    """
    Class that represents a producer.
    """

    def __init__(self, products, marketplace, republish_wait_time, **kwargs):
        """
        Constructor.

        @type products: List()
        @param products: a list of products that the producer will produce

        @type marketplace: Marketplace
        @param marketplace: a reference to the marketplace

        @type republish_wait_time: Time
        @param republish_wait_time: the number of seconds that a producer must
        wait until the marketplace becomes available

        @type kwargs:
        @param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)

        self.products = products
        self.marketplace = marketplace
        self.republish_wait_time = republish_wait_time
        self.p_id = self.marketplace.register_producer()

    def run(self):
        while 1:
            for list in self.products:
                num_of_p = 0

                while num_of_p < list[1]:
                    ret = self.marketplace.publish(str(self.p_id), list[0])

                    if ret:
                        time.sleep(list[2])
                        num_of_p += 1
                    else:
                        time.sleep(self.republish_wait_time)
