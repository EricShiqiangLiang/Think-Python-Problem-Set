def uses_all(word, string):
	for letter in string:
		if letter not in word:
			return False
	return True

key=input('Input allowed letters:\n')
word=input('Input word:\n')
print(uses_all(word, key))