# given an array, determine if it is a monotinic array

def monotone(array):
			return (all(array[i] >= array[i + 1] for i in range(len(array) -1)) or 
                    all(array[i] <= array[i + 1] for i in range(len(array) -1)))						


print(monotone([1, 2, 3, 4, 5]))
print(monotone([8, 7, 5, 4, 3]))
print(monotone([6, 6, 9, 1, 0, 7]))