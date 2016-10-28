"""
Heaps: Find the Running Median
This is used to find the running median for a continuous stream of data. Each time an element is added to the array we want the current median.

Problem definition:

    Array of numbers.
    For each number,
        print the median
            of all the numbers
                we've already seen.

Reminder:

    Median =
        Middle in sorted array.
        If two midpoints,
            median is average
                of those two.



Solutions:
    1) Each time a new element comes in, sort the whole array, and find the midpoint. This has n^2 complexity because we have to sort the array every time.
    2) Two buckets. Half the numbers in one (lower numbers), half in the other (higher numbers). Use a minHeap and a maxHeap.

Let's use solution 2.

To solve this problem we can use:
    2 heaps
        1 minHeap
        1 maxHeap

Create Heaps
    Get 0 and 1 elements
        Add min(0,  1) to maxHeap
        Add max(0,  1) to minHeap

    For each remaining element
        If element < maxHeap root:
            Add to maxHeap
        Else:
            Add to minHeap

Balance Heaps
    If a heap is bigger than other heap by more than 1
        remove root from bigger heap and add it to smaller heap

Calculate Median
    If heaps are equal size:
        median = (root of maxHeap + root of minHeap)/2
    Else
        median = root of the larger heap

Resources
    http://stackoverflow.com/questions/10657503/find-running-median-from-a-stream-of-integers
    http://stackoverflow.com/questions/33024215/built-in-max-heap-api-in-python
    https://docs.python.org/3/library/heapq.html
    Python bisect library - binary search



class Neg:
    "General negation class for maxHeap."
    def __init__(self, x):
        self.x = -x
    def __cmp__(self, other):
        return -cmp(self.x, other.x)

"""
import heapq


def add_num(num, lowers, highers):
    """
    Use negative number to emulate a maxHeap
    because maxHeap not builtin to Python
    """
    if (not lowers) or (-num > lowers[0]):
        heapq.heappush(lowers, -num)
    else:
        heapq.heappush(highers, num)
    print("Number added", num, lowers, highers)

def rebalance(lowers, highers):
    bigger, smaller = get_bigger_smaller(lowers, highers)

    if len(bigger) - len(smaller) >= 2: # if the heaps are unbalanced
        print("Heaps are unbalanced:", smaller, bigger)
        print("Move bigger heap root to smaller heap:")
        root = -heapq.heappop(bigger)
        print("{} -> {} -> {}".format(bigger, root, smaller))
        heapq.heappush(smaller, root)
        print("Balanced heaps:", bigger, smaller)

def get_bigger_smaller(lowers, highers):
    """
    Compares array length, returns (bigger, smaller)
    """
    flag = (len(lowers) > len(highers))
    bigger = lowers if flag else highers
    smaller = highers if flag else lowers
    return bigger, smaller

def median(lowers, highers):
    print("Getting median.")
    bigger, smaller = get_bigger_smaller(lowers, highers)
    if len(bigger) > len(smaller):
        return abs(bigger[0])
    else:
        print("Equal heap size, get average: {}, {}".format(abs(bigger[0]), abs(smaller[0])))
        return (float(abs(bigger[0]) + abs(smaller[0])) / 2)

def running_median(a):
    lowers, highers = [], []
    for num in a:
        add_num(num, lowers, highers)
        rebalance(lowers, highers)
        yield float(round(median(lowers, highers), 1))


for m in running_median([12, 4, 5, 3, 8, 7]):
    print(m)

