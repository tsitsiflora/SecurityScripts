# this script removes duplicates from a sorted list

# using sets
def remove_duplicates(array):
    new_array = set(array)
    return new_array

array = [1, 2, 3, 3, 4, 5, 5, 6, 5, 3, 0]
print(remove_duplicates(array))