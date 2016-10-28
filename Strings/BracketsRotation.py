import re
from itertools import combinations

def remove_valid(S):
    S1 = S
    while len(S1):
        S2 = re.sub('\{\}|\[\]|\(\)', '', S1)
        if S2 != S1:
            S1 = S2
        else:
            break
    return S1

def modify(arr, K):
    brackets = {
        '(': ')',
        ')': '(',
    }
    arr = list(remove_valid("".join(arr)))
    for i in range(1, K+1): # elements we can change
        # print(20, i)
        for indexes in combinations(range(len(arr)), i):
            temp = arr[:]
            for j in indexes:
                # print(24, j)
                temp[j] = brackets[arr[j]]
            # print(26, temp)
            temp_str = "".join(temp)
            temp_str2 = remove_valid(temp_str)
            if temp_str != temp_str2: # updated
                arr = list(temp_str2)
                return arr, i
    return arr, 0


def solution(S, K=0):
    if K == 0:
        arr_updated = remove_valid(S)
        return len(S) - len(arr_updated)

    arr = list(S)
    arr_updated = arr

    while True:
        _arr, operations = modify(arr_updated, K)
        if _arr != arr_updated:
            arr_updated = _arr
            K -= operations
        else:
            break
    return len(arr) - len(arr_updated)




assert solution(")()()(", 1) == 4
assert solution('()()()()()', 0) == 10

"""
This test fails because we are looking for
the longest CONTINUOUS substring that is valid,
whereas the algorithm removes valid brackets indiscriminately,
wherever they are, and instead returns the length
of all valid bracket combinations combined.

assert solution('(()))))(()((()))', 1) == 8


"""
[[
2
][
[]

2
['[','}','}','[']
['[','[']
0
1
2
3
0,1
0,2
0,3
1,2
1,3
2,3





A bracket sequence is considered to be a valid bracket expression if any of the following conditions is true:

        it is empty;
        it has the form "(U)" where U is a valid bracket sequence;
        it has the form "VW" where V and W are valid bracket sequences.

For example, the sequence "(())()" is a valid bracket expression, but "((())(()" is not.

You are given a sequence of brackets S and you are allowed to rotate some of them. Bracket rotation means picking a single bracket and changing it into its opposite form (i.e. an opening bracket can be changed into a closing bracket and vice versa). The goal is to find the longest slice (contiguous substring) of S that forms a valid bracket sequence using at most K bracket rotations.

Write a function:

    def solution(S, K)

that, given a string S consisting of N brackets and an integer K, returns the length of the maximum slice of S that can be transformed into a valid bracket sequence by performing at most K bracket rotations.

For example, given S = ")()()(" and K = 3, you can rotate the first and last brackets to get "(()())", which is a valid bracket sequence, so the function should return 6 (notice that you need to perform only two rotations in this instance, though).

Given S = ")))(((" and K = 2, you can rotate the second and fifth brackets to get ")()()(", which has a substring "()()" that is a valid bracket sequence, so the function should return 4.

Given S = ")))(((" and K = 0, you can't rotate any brackets, and since there is no valid bracket sequence with a positive length in string S, the function should return 0.

Assume that:

        string S contains only brackets: '(' or ')';
        N is an integer within the range [1..30,000];
        K is an integer within the range [0..N].

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
"""