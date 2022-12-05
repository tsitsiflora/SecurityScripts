#Write a function called divide_or_square that takes one
#argument (a number), and returns the square root of the number
#if it is divisible by 5, returns its remainder if it is not divisible by
#5.


def divide_or_square(n):
    if n % 5 == 0:
        square_root = n ** 0.5
        return f'The square root is {square_root}'
    else: 
        remainder = n % 5
        return f'The remainder is {remainder}'

print(divide_or_square(14))