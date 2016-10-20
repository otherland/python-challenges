from functools import update_wrapper

def decorator(d):
    """
    Decorator for decorators that ensures the wrapped
    function has the correct doc, arguments, name, etc.

    Make function d a decorator: d wraps a function fn.
    """
    return lambda fn: update_wrapper(d(fn), fn)

decorator = decorator(decorator)


@decorator
def print_result(f):
    "Decorator that prints the function result."
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        print("Result:", result)
        return result
    return wrapper

