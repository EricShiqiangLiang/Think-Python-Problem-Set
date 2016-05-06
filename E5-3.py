def is_triangle(a, b, c):
	"""a, b, c are three lengths in the same unit
	"""
	if a + b > c and a + c > b and b + c > a:
		print("Yes")
	else:
		print("No")

def check():
	a = input("Input thre sides:\n")
	b = input()
	c = input()
	is_triangle(int(a), int(b), int(c))

check()