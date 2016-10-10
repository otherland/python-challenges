"""
Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.
"""
from collections import Counter

a = "abec"
b = "abec"

ct_a = Counter(a)
ct_b = Counter(b)

ct_a.subtract(ct_b)

# get all values
# make them absolute to represent each operation done
# sum the operations
print(sum(abs(i) for i in ct_a.values()))

"""
Counter.subtract.__doc__

Like dict.update() but subtracts counts instead of replacing them.
        Counts can be reduced below zero.  Both the inputs and outputs are
        allowed to contain zero and negative counts.

        Source can be an iterable, a dictionary, or another Counter instance.

        >>> c = Counter('which')
        >>> c.subtract('witch')             # subtract elements from another iterable
        >>> c.subtract(Counter('watch'))    # subtract elements from another counter
        >>> c['h']                          # 2 in which, minus 1 in witch, minus 1 in watch
        0
        >>> c['w']                          # 1 in which, minus 1 in witch, minus 1 in watch
        -1
        >>> c
        Counter({'h': 0, 'i': 0, 'a': -1, 'w': -1, 'c': -1, 't': -2})
"""