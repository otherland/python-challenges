"""
User Instructions

Write a function, longest_subpalindrome_slice(text) that takes
a string as input and returns the i and j indices that
correspond to the beginning and end indices of the longest
palindrome in the string.

Grading Notes:

You will only be marked correct if your function runs
efficiently enough. We will be measuring efficency by counting
the number of times you access each string. That count must be
below a certain threshold to be marked correct.

Please do not use regular expressions to solve this quiz!

"""


"""
IMPLEMENTATION ONE
"""
def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if len(text) == 0: return (0, 0)
    text = text.lower()
    for i, j in longest_slice(text):
        # print(i, j)
        s = text[i:j]
        if s == s[::-1]:
            return (i, j)

def longest_slice(s):
    """
    Generator that yields all slice combinations (start, end)
    starting with the longest slice
    """
    n = len(s)
    k = 0
    while k < n-1:
        i = 0
        j = k
        while i <= k:
            yield (i, n-j)
            i += 1
            j -= 1
        k += 1


"""
IMPLEMENTATION TWO: FASTER
"""
def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    text = text.lower()
    if text == '': return (0, 0)
    """
    Iterate over all the consecutive pairs:
    [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3) ...]
    If they are palindromic, "grow" them outwards until they are not.
    """
    candidates = [grow(text, start, end)
                  for start in range(len(text))
                  for end in (start, start+1)]
    return max(candidates, key=lambda text: text[1] - text[0])

def grow(text, start, end):
    while (start > 0 and end < len(text)
        and text[start-1] == text[end]):
        # print(start, end)
        start -= 1
        end += 1
    return (start, end)




def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

# test()

