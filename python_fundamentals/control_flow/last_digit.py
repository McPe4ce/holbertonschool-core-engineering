#!/usr/bin/env python3

number = __import__('random').randint(-10000, 10000)
last_n = number % 10

if last_n > 5:
    print(f"Last digit of {number} is {last_n} and is greater than 5")

if last_n == 0:
    print(f"Last digit of {number} is {last_n} and is 0")

if last_n < 6 and last_n != 0:
    print(f"Last digit of {number} is {last_n} and is less than 6 and not 0")
