"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2021
"""
from threading import Lock, currentThread


class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """
    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        self.max_size = queue_size_per_producer
        self.producers = {}
        self.p_index = 0
        self.carts = {}
        self.c_index = 0

        self.lock_register = Lock()
        self.lock_carts = Lock()


    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        with self.lock_register:
            p_id = self.p_index
            self.producers[p_id] = []
            self.p_index += 1

        return p_id


    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        p_id = int(producer_id)

        if len(self.producers[p_id]) >= self.max_size:
            return False

        self.producers[p_id].append(product)

        return True

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        with self.lock_carts:
            c_id = self.c_index
            self.carts[c_id] = []
            self.c_index += 1

        return c_id


    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        c_id = int(cart_id)

        for i in range(0, len(self.producers)):
            for prod in self.producers[i]:
                if product == prod:
                    self.producers[i].remove(product)
                    self.carts[c_id].append(product)
                    return True

        return False


    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        c_id = int(cart_id)

        if product in self.carts[c_id]:
            self.carts[c_id].remove(product)
            self.producers[self.p_index - 1].append(product)
            return True

        return False

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        c_id = int(cart_id)

        cart = self.carts.pop(c_id, None)

        for p in cart:
            print("{} bought {}".format(currentThread().getName(), p))

        return cart
