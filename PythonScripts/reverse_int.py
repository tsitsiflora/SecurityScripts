# given an integer, return the integer in reverse

def reverse_integer(num):
	num = str(num)
	if num[0] == '-':     
		return int('-' + num[:0:-1])
	else: 
		return int(num[::-1])
	
print(reverse_integer(5437))
print(reverse_integer(-678))