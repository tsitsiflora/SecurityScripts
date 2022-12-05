# Write a function that takes a list of
# strings as an argument. The function should check if the list has
# any duplicates. If there are duplicates, the function should return
# the duplicates. If there are no duplicates, the function should
# return "No duplicates".

def duplicates(l: list):
    dup = {x for x in l if l.count(x) > 1}
    return dup

numbers = [1, 3, 5, 7, 2, 4, 1, 5, 2, 4, 2]
print(duplicates(numbers))