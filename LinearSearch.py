"""
Procedure LINEAR-SEARCH(A, n, x)

Inputs:
A: an array.
n: the number of elements in A to search through. x: the value being searched for.

Output: Either an index i for which A[i] == x, or the special value NOT-FOUND, which could be any invalid index into the array, such as 0 or any negative integer.

1. Set answer to NOT-FOUND.
2. For each index i,going from 1 to n, in order:
    A. If A[i] == x, then set answer to the value of i.
3. Return the result.

"""

def solution(A:list, n:int, x:int) -> int:
    result = -1
    n = min(len(A), n+1)
    for i in range(0, n):
        if A[i] == x:
            return i
    return result

A1 = [1,3,4,5,6]
print(solution(A1, 5, 5))


