import math

def mysqrt(a):
	x = 1.0
	while True:
		y = (x + a/x) / 2
		if abs(y - x) < 0.0001:
			break
		x = y
	return y

print('a'+' '*4 + 'mysqrt(a)' + ' '*5 + 'diff')
for i in range(1, 10):
	a = i * 1.0
	y = mysqrt(a)
	z = math.sqrt(a)
	diff = abs(y - z)
	print ('%.1f %.11f %.11f' %(a, y, diff))