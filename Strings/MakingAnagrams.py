"""
Strings: Making Anagrams

Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make and anagrams. Any characters can be deleted from either of the strings.
"""
from collections import Counter

def solution(a, b):
    cnt = Counter(a)
    print(cnt)

    cnt.subtract(b)
    print(cnt)

    operations = [abs(i) for i in cnt.values()]
    print(operations)

    return sum(operations)

a = "cde"
b = "abc"
assert solution(a, b) == 4