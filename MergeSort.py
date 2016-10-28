"""
MergeSort

O(n log n) time
O(n) space

Downside: requires extra memory


1) Split array in A and B, evenly
2) Sort either A and B, separately
3) Traverse A and B
    a) compare A[0] with B[0]
    b) add smaller to result array


"""

def merge(A, B):
    C = []
    while A and B:
        if A[0] >= B[0]:
            C.append(B.pop(0))
        else:
            C.append(A.pop(0))
    if A:
        C.extend(A)
    elif B:
        C.extend(B)
    return C

def mergesort(array):
    C = []
    for i in range(0, len(array), 2):
        merged = merge([array[i]],[array[i+1]])
        print(merged)
        C.extend(merged)
    return C




r = solution([2, 9, 1, 8, 10, 6, 5, 7, 4, 3])
print(r)