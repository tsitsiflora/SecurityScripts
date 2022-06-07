# this script looks for the majority element in a given list

def check_majority(array, n):
    map = {}
    for i in range(0, n):
        if array[i] in map.keys():
            map[array[i]] += 1
        else:
            map[array[i]] = 1
    
    for key in map:
        if map[key] >= (n / 2):
            return key
    
    return -1

array = [2, 3, 7, 7, 3, 4, 4, 2, 5, 4]
n = len(array)
ans = check_majority(array, n)

if ans != -1:
    print(f"The majority item is {ans}.")
else:
    print("There is no majority item.")

