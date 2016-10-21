"""
https://www.interviewcake.com/question/python/product-of-other-numbers

You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

[1, 7, 3, 4]

your function would return:

[84, 12, 28, 21]

by calculating:

[7*3*4, 1*3*4, 1*7*4, 1*7*3]

Do not use division in your solution.

"""

def get_products_of_all_ints_except_at_index(arr):

    return arr

x = [1, 7, 3, 4]
print(get_products_of_all_ints_except_at_index(x))



"""
We're doing some of the same multiplications two or three times!
When we calculate [2*6*5*9, 1*6*5*9, 1*2*5*9, 1*2*6*9, 1*2*6*5], we're calculating 5*9 three times: at indices 0, 1, and 2.

Or look at this pattern:
When we calculate [2*6*5*9, 1*6*5*9, 1*2*5*9, 1*2*6*9, 1*2*6*5], we have 1 in index 1, and we calculate 1*2 at index 2, 1*2*6 at index 3, and 1*2*6*5 at index 4.

We’re redoing multiplications when instead we could be storing the results! This would be a great time to use a greedy ↴ approach. We could store the results of each multiplication highlighted in blue, then just multiply by one new integer each time.

So in the last highlighted multiplication, for example, we wouldn’t have to multiply 1∗2∗61*2*61∗2∗6 again. If we stored that value (121212) from the previous multiplication, we could just multiply 12∗512*512∗5.

Can we break our problem down into subproblems so we can use a greedy approach?

"""