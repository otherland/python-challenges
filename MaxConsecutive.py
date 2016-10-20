"""
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.
"""


def solution(n):
    # Split into sequences of 1s and get the len of the longest sequence
    ones = format(n, 'b').split('0')
    return len(max(ones))


def solution2(n):
    """
    5869 = 1011011101101
    << 1 = 0110111011010 = 11738
    &    = 0010001100100 =  1124

    << 1 = 0100011001000
    &    = 0000001000000 =   128

    <<1  = 0000100000000
    &    = 0000000000000 =     0
    """
    count = 0

    while n:
        n = (n & (n << 1))
        count += 1
    return count


def solution3(n):
    b = list(format(n, 'b'))
    max_consecutive = 0
    count = 0
    for i in b:
        if i == '1':
            count += 1
        else:
            max_consecutive = max(max_consecutive, count)
            count = 0
    max_consecutive = max(max_consecutive, count)
    return max_consecutive


assert solution(5) == 1 # '101'
assert solution(13) == 2 # '1101'