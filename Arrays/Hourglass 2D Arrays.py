def solution(X):
    # Flatten array
    # X = list(map(int, X.replace("\n", " ").strip().split()))

    hg = [0, 1, 2, 7, 12, 13, 14] # Hourglass integers

    # Starting points
    g = [k for m in [range(i,i+4) for i in range(0,19,6)] for k in m]

    # Hourglasses
    h = [[X[i+j] for j in hg] for i in g]
    r = max(sum(q) for q in h)
    return r

def solution(arr):
    arr = [[int(j) for j in i.split()] for i in X.strip().split('\n')]
    res = []
    for x in range(0, 4):
        for y in range(0, 4):
            top = arr[x][y:y+3]
            middle = arr[x+1][y+1]
            bottom = arr[x+2][y:y+3]
            s = sum(top) + middle + sum(bottom)
            res.append(s)

    return max(res)




X = """
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
"""
assert solution(X) == 19


"""
Context
Given a 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

Input Format

There are 6 lines of input, where each line contains space-separated integers describing 2D Array A; every value in A will be in the inclusive range of -9 to 9.


Output Format

Print the largest (maximum) hourglass sum found in A.

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output

19

Explanation

A contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

The hourglass with the maximum sum (19) is:

2 4 4
  2
1 2 4
"""