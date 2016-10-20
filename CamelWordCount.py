
word_count = lambda s : 1 + sum(map(str.isupper, s))

assert word_count('helloWorld') == 2

"""
Count the words in a camelCase string

Constraints:
len(s) >= 1
"""