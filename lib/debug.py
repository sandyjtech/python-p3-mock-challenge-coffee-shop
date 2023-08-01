#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

sandy = Customer("Sandy")
latte = Coffee("latte")
mocha = Coffee("mocha")

order1 = Order(sandy, latte, 2)
order2 = Order(sandy, latte, 6)
order3 = Order(sandy, mocha, 9)
if __name__ == '__main__':
    print("HELLO! :) let's debug")

    ipdb.set_trace()
