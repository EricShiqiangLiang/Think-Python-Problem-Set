def is_abecedarian(word):
	pre = word[0]
	for letter in word[1:]:
		if letter < pre:
			return False
		pre = letter
	return True

print(is_abecedarian('abcd'))
print(is_abecedarian('abccd'))
print(is_abecedarian('ba'))