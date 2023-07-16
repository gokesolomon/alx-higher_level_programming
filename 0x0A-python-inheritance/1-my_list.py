#!/usr/bin/python3
"""class MyList that inherits list
"""


class MyList(list):
    """inherits list"""
    def print_sorted(self):
        """prints the list, but sorted
        (ascending sort)
        """
        print(sorted(self))
