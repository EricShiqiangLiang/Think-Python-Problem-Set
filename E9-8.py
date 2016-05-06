def is_palindrome(word):
	if word[0:] == word[::-1]:
		return True 
	else:
		return False

for i in range(100000,999996):
	if is_palindrome(str(i)[2:]) and is_palindrome(str(i+1)[1:]) and is_palindrome(str(i+2)[1:-1]) and is_palindrome(str(i+3)):
		print(i)

