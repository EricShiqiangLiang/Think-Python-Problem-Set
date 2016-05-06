import math

def estimate_pi():
	res = 0
	k = 0
	while True:
		num = math.factorial(4*k) * (1103 + 26390 * k)
		denom = math.pow(math.factorial(k), 4) * math.pow(396, 4*k)
		res = num/denom + res
		k = k + 1
		if num/denom < 1e-15:
			break
	return 1/(res*2*math.sqrt(2)/9801)

print(math.pi)
print(estimate_pi())
