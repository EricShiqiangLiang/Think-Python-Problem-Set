def uses_only(word, string):
	for letter in word:
		if letter not in string:
			return False
	return True

key=input('Input allowed letters:\n')
word=input('Input word:\n')
print(uses_only(word, key))