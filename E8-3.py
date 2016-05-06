def is_palindrome(word):
	if word[0:] == word[::-1]:
		return True 
	else:
		return False

a="12345"
print(a[::-1])

print(is_palindrome('KK'))