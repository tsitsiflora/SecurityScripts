# given a target number, this script goes through an
# array and returns 2 numbers in the array that add up 
# to the target

def sum_of_two(array, target):
    res = {}
    for i in range(len(array)):
        if target - array[i] in res:
            return [res[target - array[i]], i]
        else:
            res[array[i]] = i


input_list = [2, 5, 4, 3, 7, 10]
target = 13
print(sum_of_two(input_list, target))

