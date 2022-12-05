# Write a function that takes a dictionary
# as an argument and returns the first longest value of the
# dictionary.

def longest_value(d: dict):
    longest = max(d.values(), key =len)
    return longest
    
numbers = {"first": "first", "second": "second"}
print(longest_value(numbers))