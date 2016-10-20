from HelperFunctions import decorator


@decorator
def memo(f):
    """
    Memoization. Stores a function result in
    a cache (dictionary).
    """
    cache = {}
    def _f(*args):
        try:
            result = cache[args]
            print("Result in cache")
            return result
        except KeyError:
            # Args not cached yet, run function, cache, return result
            print("Result not cached")
            cache[args] = result = f(*args)
            return result
        except TypeError:
            print("Cannot cache")
            # Args are not hashable; we can't cache them
            return f(*args)
    return _f

# @decorator
# def count_calls(f):
#     def wrapper(*args, **kwargs):
#         wrapper.calls += 1
#         return f(*args, **kwargs)
#     wrapper.calls = 0
#     return wrapper

# @decorator
# def count_calls(f):
#     "Decorator that makes the function count calls to it."
#     def wrapper(*args, **kwargs):
#         callcounts[wrapper] += 1
#         return f(*args, **kwargs)
#     callcounts[wrapper] = 0
#     return wrapper
# callcounts = {}



@memo
def add(x, y):
    print("Calling add")
    return x+y


add(2, 3)
add(2, 3)
add(3, 4)
add(3, 4)
