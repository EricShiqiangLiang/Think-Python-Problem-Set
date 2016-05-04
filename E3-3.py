def row1():
	print('+ - - - -', end=' ')

def row2():
	print('|        ', end=' ')

def endrow1():
	print('+')

def endrow2():
	print('|')

def do_x(f, x):
	for i in range(0, x):
		f()

def do_y(f, y, s):
	for i in range(0, y):
		f(s)

def grid1(column):
	do_x(row1, column-1)
	endrow1()
	do_x(row2, column-1)
	endrow2()
	do_x(row2, column-1)
	endrow2()
	do_x(row2, column-1)
	endrow2()
	do_x(row2, column-1)
	endrow2()

def grid2(row, column):
	do_y(grid1, row-1, column)
	do_x(row1, column-1)
	endrow1()

grid2(4, 4)