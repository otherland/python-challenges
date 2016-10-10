def heapsort(sequence):
    sequence_length = len(sequence)
    print('Sequence length:', sequence_length)

    def swap_if_greater(parent_index, child_index):
        print('Running swap if greater...\n')
        if sequence[parent_index] < sequence[child_index]:
            print('Swapping elements because parent_index is less than child_index')
            sequence[parent_index], sequence[child_index] =\
                    sequence[child_index], sequence[parent_index]
            print('Sequence:', sequence)

    def sift(parent_index, unsorted_length):
        print('Running sift...\n')

        index_of_greater = lambda a, b: a if sequence[a] > sequence[b] else b
        while parent_index*2+2 < unsorted_length:
            print('Parent index:', parent_index)
            print('parent_index*2+2 :', parent_index*2+2)
            left_child_index = parent_index*2+1
            right_child_index = parent_index*2+2
            print('Left child index:', left_child_index)
            print('Right child index:', right_child_index)
            greater_child_index = index_of_greater(left_child_index,
                    right_child_index)
            print('Greater child index:', greater_child_index)

            swap_if_greater(parent_index, greater_child_index)

            parent_index = greater_child_index

    def heapify():
        arr = range((sequence_length//2)-1, -1, -1)
        print('arr:', list(arr))
        for i in arr:
            sift(i, sequence_length)

    def sort():
        print('Running sort...\n')
        arr = range(sequence_length-1, 0, -1)
        print('arr:', list(arr))
        for i in arr:
            swap_if_greater(i, 0)
            sift(0, i)

    heapify()
    print('Finished heapify:', sequence)
    sort()

from random import shuffle
sequence = list(range(15))
shuffle(sequence)
print(sequence)
heapsort(sequence)