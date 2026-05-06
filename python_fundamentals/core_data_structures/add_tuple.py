#!/usr/bin/env python3

# :2 means to stop at the second integer of the tuple only
# (0, 0) gives O to empty spots
# add the index of each tuples between them

def add_tuple(tuple_a=(), tuple_b=()):
    first_turtle = tuple_a[:2] + (0, 0)
    sec_turtle = tuple_b[:2] + (0, 0)
    return (first_turtle[0] + sec_turtle[0], first_turtle[1] + sec_turtle[1])


if __name__ == "__main__":
    print(add_tuple((1, 89), (88, 11)))
    print(add_tuple((1, 89), (1, )))
    print(add_tuple((1, 89), ()))
    print(add_tuple((), ()))
