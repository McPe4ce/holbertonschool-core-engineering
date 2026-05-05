#!/usr/bin/env python3

def pow(a, b):
    result = 1
    power = abs(b)

    for _ in range(power):
        result *= a

    if b < 0:
        return 1 / result
    return result
    