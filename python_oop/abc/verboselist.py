#!/usr/bin/env python3
"""Module that creates a verbose list, extending the basic list class"""


class VerboseList(list):

    def append(self, object):
        print(f"Added [{object}] to the list")
        return super().append(object)

    def extend(self, iterable):
        print(f"Extended the list with [{iterable}] items.")
        return super().extend(iterable)

    def remove(self, value):
        if value in self:
            print(f"Removed [{value}] from the list.")
            return super().remove(value)

    def pop(self, index=-1):
        if -len(self) <= index < len(self):
            value = super().pop(index)
            print(f"Popped [{value}] from the list.")
            return value
        else:
            print(f"[{value}] isnt in the list")
