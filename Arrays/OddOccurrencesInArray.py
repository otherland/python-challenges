
"""
Find value that occurs in odd number of elements.
"""


# 10000 loops, best of 3: 35.8 µs per loop
from collections import Counter

def solution(A):
  odd_values = next((i for i in Counter(A).items() if i[1] % 2 != 0), False)
  return odd_values[0] if odd_values else 0



# 10000 loops, best of 3: 23.4 µs per loop
def solution(A):
  A.sort()
  for i in range(0, len(A) -1, 2):
    if A[i] != A[i+1]:
      return A[i]
  return 0



# 10000 loops, best of 3: 43.5 µs per loop
def solution(A):
    """
    The XOR (^) or exclusive or operator compares two numbers
    on a bit level and returns a number where the bits of that
    number are turned on if either of the corresponding bits
    of the two numbers are 1, but not both.
    """
    missing = 0
    for i in A:
        missing ^= i
    return missing



assert solution([9,3,9,3,9,7,9]) == 7



"""
A non-empty zero-indexed array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

        the elements at indexes 0 and 2 have value 9,
        the elements at indexes 1 and 3 have value 3,
        the elements at indexes 4 and 6 have value 9,
        the element at index 5 has value 7 and is unpaired.

Write a function:

    def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

the function should return 7, as explained in the example above.

Assume that:

        N is an odd integer within the range [1..1,000,000];
        each element of array A is an integer within the range [1..1,000,000,000];
        all but one of the values in A occur an even number of times.

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

"""