#!/usr/bin/env python3

class Coffee:

    def __init__(self, size, price):
        if not size:
            raise ValueError("size is required")

        sizes = ["Small", "Medium", "Large"]

        if size.capitalize() not in sizes:
            raise ValueError("size must be Small, Medium or Large")

        if not price:
            raise ValueError("price is required")

        if not isinstance(price, int):
            raise ValueError("price must be an integer")

        self.size = size
        self.price = price

    def tip(self):
        print("This coffee is great, here’s a tip")
        self.price += 1
