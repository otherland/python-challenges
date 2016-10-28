"""
https://www.interviewcake.com/question/python/product-of-other-numbers

You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function solution() that takes a list of integers and returns a list of the products.

For example, given:

[1, 7, 3, 4]

your function would return:

[84, 12, 28, 21]

by calculating:

[7*3*4, 1*3*4, 1*7*4, 1*7*3]

Do not use division in your solution.

"""

def solution_1(arr):
    increase = []
    decrease = []
    result = []
    size = len(arr)
    last = 1
    for i in arr:
        last *= i
        increase.append(last)
    last = 1
    for j in reversed(arr):
        last *= j
        decrease.append(last)
    for index in range(size):
        if index == 0:
            k = decrease[-2]
        elif index == size - 1:
            k = increase[-2]
        else:
            left = increase[index-1]
            right = decrease[size-index-2]
            k = left * right
        result.append(k)
    return result



def solution_2(arr):

    # for each integer, find the product of all the integers
    # before it, storing the total product so far each time
    before = [] # products_of_all_ints_before_index
    product = 1
    for i in arr:
        before.append(product)
        product *= i

    product = 1

    for j in range(len(arr)-1, -1, -1):
        before[j] *= product
        product *= arr[j]

    return before


# Tests
assert solution_2([1, 7, 3, 4]) == [84, 12, 28, 21]

print('Tests pass.')



"""

solution_2 Complexity

O(n) time and O(n) space. We make two passes through our input a list, and the list we build always has the same length as the input list.


What We Learned

Another question using a greedy approach. The tricky thing about this one: we couldn't actually solve it in one pass. But we could solve it in two passes!

This approach probably wouldn't have been obvious if we had started off trying to use a greedy approach.

Instead, we started off by coming up with a slow (but correct) brute force solution and trying to improve from there. We looked at what our solution actually calculated, step by step, and found some repeat work. Our final answer came from brainstorming ways to avoid doing that repeat work.

So that's a pattern that can be applied to other problems:

Start with a brute force solution, look for repeat work in that solution, and modify it to only do that work once.

"""


