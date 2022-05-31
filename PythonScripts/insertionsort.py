# insertion sort algorithm
# time complexity: O(n^2)

def insertion_sort(array):
    # loop from the second element in the 
    # array until the last element
    for i in range(1, len(array)):
        # this is the item we want to position in it's
        # correct spot
        key_item = array[i]

        # initialize the variable that will be used to 
        # find the correct posiion of the key_item
        j = i - 1

        # go through the left potion of the array
        # and find the correct position for the key_item
        while j >= 0 and array[j] > key_item:
            #shift the value one position to the left
            # and reposition j to point to the next element
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array 

array = [9, 2, 5, 3, 1, 7, 4]
print(insertion_sort(array))