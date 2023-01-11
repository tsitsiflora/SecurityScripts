# Write a function that takes a single
# number and returns a string of its range. The string characters
# should be separated by dots(.)

def string_range(n):
    x = [str(i) for i in range(n)]
    y = ".".join(x)
    return y


print(string_range(7))