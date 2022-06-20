# given 2 sentences, return words that appear in one 
# sentence and not the other, and common words

def word_play(s1, s2):
	set1 = set(s1.split())
	set2 = set(s2.split())
	return set1 ^ set2, set1 & set2


s1 = "This is a cat."
s2 = "This is a dog."
print(word_play(s1, s2))