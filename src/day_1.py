"""
Day 1 : Division and Square Root 
"""
import math


def divide_or_square(number) -> float:
    if number % 5 == 0:
        return round(math.sqrt(number), 2)
    else:
        return number % 5

print(divide_or_square(10))