# given a word, return the first non-repeating character in that word

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
    
   
		
  


print(unique_character("abracadabra"))
print(unique_character("maam"))