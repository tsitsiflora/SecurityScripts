# Write a function that takes a list of numbers
# as an argument. The code should zero (0) the first and the last
# number in the list.

def zeroed(l: list):
    l[0] = 0
    l[- 1] = 0
    return l

print(zeroed([2, 4, 6, 8, 10]))