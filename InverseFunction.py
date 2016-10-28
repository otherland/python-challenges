"""
Write a function, inverse, which takes as input a monotonically increasing (always increasing) function that is defined on the non-negative numbers. The runtime of your program should be proportional to the LOGARITHM of the input.

You may want to do some research into binary search and Newton's method to help you out.

This function should return another function which computes the inverse of the input function.

Your inverse function should also take an optional parameter, delta, as input so that the computed value of the inverse will be within delta of the true value.
"""



"""
----------------------------------------
SOLUTION 1 - SLOW
"""
def slow_inverse(f, delta=1/128.):
    def f_1(y):
        x = 0
        while f(x) < y:
            # print(x, f(x))
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1



"""
----------------------------------------
SOLUTION 2 - BETTER
"""
def inverse(f, delta = 1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def _f(y):
        _min = delta
        _max = y
        r = 1
        while True:
            average = (_min + _max)/2
            r = f(average)
            # print(average)
            if round(r, 6) == y:
                break
            elif r > y:
                _max = average - delta
            elif r < y:
                _min = average + delta
        return average if (f(average)-y < y-f(average-delta)) else r-delta
    return _f


"""
----------------------------------------
SOLUTION 3 - Peter Norvig
"""
def inverse(f, delta=1/1024.):
    def _f(y):
        lo, hi = find_bounds(f, y)
        return binary_search(f, y, lo, hi, delta)
    return _f

def find_bounds(f, y):
    """
    Find values lo, hi such that f(lo) <= y and f(hi) >= y
    Keep doubling hi until f(hi) >= y; that's hi
    Lo will be 0 or previous hi, which is new hi divided by 2 because we've just doubled it.
    """
    hi = 1.
    while f(hi) < y:
        hi = hi * 2.
    lo = 0 if (hi == 1) else hi/2
    return lo, hi

def binary_search(f, y, lo, hi, delta):
    """
    Given f(lo) <= y <= f(hi), return x such that f(x) is within delta of y.
    Our target x is between lo and hi, we need to narrow down until we get the correct result.
    """
    while lo <= hi:
        x = (lo + hi) / 2
        r = f(x)
        if r > y:
            hi = x - delta
        elif r < y:
            lo = x + delta
        else:
            return x
    return hi if (f(hi)-y < y-f(lo)) else lo




def square(x): return x**2
def pow10(x): return x**10
def cube(x): return x**3


sqrt = inverse(square)
log10 = inverse(pow10)
cuberoot = inverse(cube)

print(sqrt(1000000000))
