#!/usr/bin/env python3
# $ pytest -x testing/shoe_test.py
class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # private variable to store size
        # Set the size using the setter method
        self.size = size
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
    pass