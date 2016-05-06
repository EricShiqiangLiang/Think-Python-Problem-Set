import math

def check_fermat(a, b, c, n):
	if pow(a, n) + pow(b, n) == pow(c, n) and n > 2:
		print("Holy smokes, Fermat was wrong!")
	else:
		print("No, that doesn't work.")

def check():
	a = input("Input values for a, b, c and n:\n")
	b = input()
	c = input()
	n = input()
	check_fermat(int(a),int(b),int(c),int(n))

check()