# an implementation of ROT13, a couple of ways
# ROT13 is just ceasar cipher with a constant key of 13

# 1. using chr and ord and list comprehensions
def rot_13(sentence):
    return ''.join([chr((ord(letter) - 97 + 13) % 26 + 97)
                    for letter in sentence.lower()])

print(rot_13("python"))


# 2. using string for index and mapping
import string

def rot13(sentence):
    alphabet = string.ascii_lowercase
    return ''.join([alphabet[(alphabet.find(letter) + 13) % 26]
                        if alphabet.find(letter) >= 0 else letter
                    for letter in sentence.lower()])

print(rot13("this Is my Name"))