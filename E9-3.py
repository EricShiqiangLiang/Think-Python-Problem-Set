def avoids(word, key):
	for letter in key:
		if letter in word:
			return False
	return True

key=input('Input forbidden letters:\n')
word=input('Input word:\n')
print(avoids(word, key))