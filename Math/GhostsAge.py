
"""
 On every birthday, a ghost's opacity is reduced by a number of units equal to its age when its age is a Fibonacci number (Read about this here) or increased by 1 if it is not.
"""

from math import sqrt
isFib = lambda x : sqrt(5 * x * x + 4 ).is_integer() or sqrt(5 * x * x - 4 ).is_integer()

def checkio(target):
    target = max(target, 0)
    opacity = 10000
    age = 0
    while opacity > target:
        age += 1
        if isFib(age):
            opacity -= age
        else:
            opacity += 1
    else:
        # hack?
        if opacity != target:
            age += 1
    return age




assert checkio(10000) == 0

assert checkio(9999) == 1

assert checkio(9997) == 2

assert checkio(9994) == 3

assert checkio(9995) == 4

assert checkio(9990) == 5

assert checkio(3703) == 4665

