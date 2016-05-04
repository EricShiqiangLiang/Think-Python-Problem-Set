def do_twice1(f):
	f()
	f()

def do_twice2(f, v):
	f(v)
	f(v)

def print_twice(s):
	print(s)
	print(s)

def print_spam():
	print('spam')

def do_four(f, s):
	do_twice2(f, s)
	do_twice2(f, s)

do_four(print_twice, 'spam')