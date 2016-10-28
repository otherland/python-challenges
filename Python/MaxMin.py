def max(*args, **kwargs):
    key = kwargs.pop('key', lambda x: x)
    iterable = list(args[0]) if len(args) == 1 else args
	r = iterable[0]
	for i in iterable:
		if key(i) > key(r):
			r = i
	return r

def min(*args,key=None):
    return sorted(len(args)==1 and args[0] or args,key=key)[0]

​

def max(*args,key=None):
    return sorted(len(args)==1 and args[0] or args,key=key,reverse=True)[0]

​

if __name__ == '__main__':

    assert max(3, 2) == 3, "Simple case max"

    assert min(3, 2) == 2, "Simple case min"

    assert max([1, 2, 0, 3, 4]) == 4, "From a list"

    assert min("hello") == "e", "From string"

    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"

    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"

