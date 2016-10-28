"""
QuickSort

Runtime
    O(n log(n)) average
    O(n^2) worst case

    Because each element gets quicksort applied
    to it log(n) times.

    Worst case scenario:
        Chosen pivot element is always lowest element.
        n^2 quicksorts required.

    Aim: get the best pivot to minimise cost.




[15, 3, 9, 8, 5, 2, 7, 1, 6]
pivot = 7

Then we go through until we find a number
that is bigger than our pivot. Next we
iterate in reverse until we find an element
that is smaller than our pivot.
We then swap these numbers

15, 6
15 > pivot and 6 < pivot, so swap!
[6, 3, 9, 8, 5, 2, 7, 1, 15]

9, 1
swap!
[6, 3, 1, 8, 5, 2, 7, 9, 15]

We don't want to swap our pivot, so
when we get to 8, we jump to 2, which
is the right element we're swapping.

[6, 3, 1, 2, 5, 8, 7, 9, 15]


We then have two halves, which we'll
quicksort separately.

[6, 3, 1, 2, 5]  [8, 7, 9, 15]




"""


def partition(array:list, left:int, right:int, pivot:int) -> list:
    print("Partitioning.")
    print("Array:", array)
    print("Left:", left)
    print("Right:", right)
    print("Pivot:", pivot)
    # Move pointers in towards each other
    while left <= right:
        # Move left until element is > pivot
        while array[left] < pivot:
            print("Moving right until element < pivot.")
            left += 1

        # Move right until element < pivot
        while array[right] > pivot:
            print("Moving left until element < pivot.")
            right -= 1

        if left <= right:
            print("Swapping elements: {} {}.\n".format(array[left], array[right]))
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
            print("Moved pointers:", left, right)
    # Now...
    # Elements < pivot are before it
    # Elements > pivot are after it

    print("Returning the partition point between the smaller elements:", left)
    return left


def solution(array:list) -> list:
    n = len(array)
    def quicksort(array:list, left:int, right:int) -> list:
        print("Inside quicksort.\n")

        if left >= right:
            return array

        # pivot = center of array;
        # other methods possible
        pivot = array[(left + right) // 2]

        # Partition elements around pivot
        index = partition(array, left, right, pivot)
        print("Sort elements to left of pivot.")
        array = quicksort(array, left, index-1)

        print("Sort elements to right of pivot.\n")
        array = quicksort(array, index, right)
        return array
    return quicksort(array, 0, n-1)



# ------------------------------
# FEWER COMMENTS VERSION
# ------------------------------

def partition(array, left, right, pivot):
    while left <= right:
        while array[left] < pivot:
            left += 1

        while array[right] > pivot:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

        return left

def quicksort(array, left, right):
    if left >= right:
        return array

    # Array midpoint
    pivot = array[(left + right) // 2]

    index = partition(array, left, right, pivot)
    # Sort leftside
    array = quicksort(array, left, index-1)
    # Sort rightside
    array = quicksort(array, index, right)

    return array

def solution(array):
    n = len(array)
    return quicksort(array, 0, n-1)



r = solution([15, 3, 9, 8, 5, 2, 7, 1, 6])
print(r)