"""
Write a function that takes an array of numbers and returns the greatest difference you can get by subtracting any two of those numbers.
"""
from HelperFunctions import print_result

# @print_result
def solution(a):
    lo = a[0]
    hi = a[0]
    for i in a:
        if i > hi:
            hi = i
        elif i < lo:
            lo = i
    return hi-lo

assert solution([5,8,6,1]) == 7