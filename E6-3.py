def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	if word == '':
		return True
	else:
		if first(word) == last(word):
			return is_palindrome(middle(word))
		else:
			return False

print(middle('aa'))
print(is_palindrome('aa'))