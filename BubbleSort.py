"""
Rarely useful sorting algorithm.

Maybe use a sorted array, when one element is incremented, to re-sort on one pass through.

"""


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        currentSwaps = 0
        for j in range(0, n - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                currentSwaps += 1

        print("Current swaps", currentSwaps)
        if currentSwaps == 0:
            break
    return array


r = bubble_sort([1,5,6,4,3,2,3,6,7,5,4,3])
print(r)