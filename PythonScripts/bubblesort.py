# the bubble sort algorithm
# time complexity: O(n^2)

import random

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # create a flag that will allow the function
        # to terminate early in case the array is
        # already sorted
        already_sorted = True

        # start looking at each item one by one, first
        # compare the first 2 and bubble the larger number
        # to the right. Compare the second and third and 
        # do the same. 
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
            # if item is greater than the adjacent item,then 
            # we swap them and move the larger one right
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        # if there are no swaps in the last iteration it means the 
        # array is already sorted and we can terminate
        if already_sorted:
            break

    return array


items = [random.randint(1, 500) for _ in range(100)]
print(bubble_sort(items))
