def solution(alist):
    """
    O(n^2)
    """
    t = alist[0]
    for i in alist:
        smallest = True
        for j in alist:
            if i > j:
                smallest = False
            if smallest:
                t = i
    return t

def solution(alist):
    """
    O(n)
    """
    last = alist[0]
    for j in alist:
        if j < last:
            last = j
    return last

print(solution([2,6,3,5,1,-5]))