# given a word, return the first non-repeating character in that word

import collections

def unique_character(word):
	res = {}

	for char in word:
		if char not in res:
			res[char] = 1
		else:
			res[char] += 1

	for char in range(len(word)):
		if res[word[char]] == 1:
			return char
    
    
    
# using collections

def unique_chars(word):
    count = collections.Counter(word)
    for indx, char in enumerate(word):
        if count[char] == 1:
            return indx
    
    return -1

print(unique_character("abracadabra"))
print(unique_character("maam"))
print(unique_chars("eell"))
   
		
  


