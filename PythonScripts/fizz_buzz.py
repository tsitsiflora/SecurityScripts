#this script replaces certain numbers with certain words

def fizz_buzz(numbers):
    '''Get a list of numbers:
        1. Replace all numbers divisible by 3 with fizz
        2. Replace all numbers divisible by 5 with buzz
        3. Replace all numbers divible by both 3 and 5
        with fizzbuzz
        >>> numbers = [3, 15, 67, 45, 72, 97, 65]
        >>> fizz_buzz(numbers)
        >>> numbers
        [fizz, fizzbuzz, 67, fizzbuzz, fizz, 97, buzz]
        '''
    for i in range(len(numbers)):
        num = numbers[i]
        if num % 3 == 0:
            numbers[i] = "fizz"
        if num % 5 == 0:
            numbers[i] = "buzz"
        if num % 3 and num % 5:
            numbers[i] = "fizzbuzz"