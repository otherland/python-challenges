"""
Print the absolute difference between the two sums of the matrix's diagonals as a single integer.
"""
def solution(arr):
    leftD = 0
    rightD = 0
    size = len(arr)
    for j in range(size):
        leftD += arr[j][j]
        rightD += arr[j][size-1-j]
    return abs(leftD - rightD)


X = [
[11, 2, 4],
[4, 5, 6],
[10, 8, -12]
]

assert solution(X) == 15

"""
This solution is actually asymptotically optimal for time as well as space, a certain amount of condition checking calculations would be required for ANY solution to this problem, and the overhead of storing data to an array is much higher than doing a simple condition check on data that is already loaded into computation registers while iterating through the loop (so your argument makes no sense). To use an array, which is what it seems like you are suggesting as a better solution, would just add several layers of inefficiency and could result in additional computation time as N becomes large due to the overhead involved in needlessly storing and reloading inputs that are not needed for calculation and are not needed beyond a single calculation. Using an array also becomes increasingly inefficient as N grows, because the more space you block out (the larger the array), the harder it is to find contiguous space in memory to store that array (so a lot of behind-the-scenes time consuming data shuffling takes place).

In software engineering, algorithms get complex; part of being a good programmer is breaking down things into structured components and providing adequate documentation for your work, to both ensure you fully understand why what you did works and so others can better understand it during code review. Using an array for this is an incredibly sloppy thing to do, because there is no need for it and you would still need an algorithm to calculate the values in the array--you should not add layers of complexity to your code that have no benefit. The only reason to use an array for this type of thing would be if you knew there would be a future need to perform additional calculations on the same set of data. At my job, an attempt to use an array for something like this would be kicked back in a code review and never make it to release.
"""



