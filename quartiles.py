numbers = [1,12,43,59,87,65,44,41,42,5,7]
size = len(numbers)

lower = numbers[:size//2]
upper = numbers[size//2 + size % 2:]

def median(arr):
    size = len(arr)
    m = arr[size // 2]
    if not size % 2:
        m = (m + arr[size // 2 - 1]) / 2
    return m


q1 = median(lower)
q2 = median(arr)
q3 = median(upper)