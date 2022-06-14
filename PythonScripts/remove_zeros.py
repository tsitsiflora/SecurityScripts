# given an array, move all zeros to the end of the list

def remove_zeros(array):
	for num in array:
		if num == 0:
			array.remove(num)
			array.append(num)
	return array


print(remove_zeros([1, 0, 2, 9, 3, 0, 5, 0]))