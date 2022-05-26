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

            index_char = ord(char) - ord('A')
            new_index = (index_char + key) % 26
            new_char = chr(new_index + ord('A'))
            cipher += new_char
        else:
            cipher += char
    return cipher

def main():
    ceasar_cipher = encrypt_char('TSITSI', 3)
    print(ceasar_cipher)

if __name__ == '__main__':
    main()
