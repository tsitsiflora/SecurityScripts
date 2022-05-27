#this script is about the the substitution cipher, ceasar
# we will be using this formula: c = (x + n) % 26

def encrypt_char(text, key):
    '''The function takes plain text
    ,assigns numbers to the letters, and for
    each letter, adds the key and does a modulo with 26,
    Then returns the output.
    '''
    cipher = ''
    for char in text:
        if char.isupper():

            index_char = ord(char) - ord('A') # subtract the unicode of A to get a value in the range 0-25
            new_char = chr((index_char + key) % 26 + ord('A'))
            cipher += new_char
        
        elif char.islower():

            index_char = ord(char) - ord('a') # subtract the unicode of A to get a value in the range 0-25
            new_char = chr((index_char + key) % 26 + ord('a'))
            cipher += new_char

        elif char.isdigit():

            new_char = (int(char) + key) % 10 # if its a number, shift it's actual value
            cipher += str(new_char)

        else:
            cipher += char

    return cipher

def main():
    ceasar_cipher = encrypt_char('TSITSI is coming on the 4th', 3)
    print(ceasar_cipher)

if __name__ == '__main__':
    main()
