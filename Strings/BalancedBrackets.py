"""
A sequence of brackets is considered to be balanced if the following conditions are met:

    It contains no unmatched brackets.
    The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
"""

def is_matched(expression):
    stack = []
    hash = {'}':'{',')':'(',']':'['}
    for c in list(expression):
        if c in hash and len(stack) and stack[-1] == hash[c]:
            # matched bracket!
            stack.pop()
        else:
            stack.append(c)
        # print("Stack:", stack, "Character:", c)
    return len(stack) == 0

assert is_matched("{}()[]") == True
assert is_matched("{({}()[])}") == True
assert is_matched("{({}()[])") == False