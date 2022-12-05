# Write a function that takes a list of strings
# as an argument and converts it to integers and sums the list.

def convert_add(l: list):
    new_list = []
    for i in l:
        new_list.append(int(i))
    
    return sum(new_list)


numbers = ["6", "4", "0", "5", "1"]
print(convert_add(numbers))