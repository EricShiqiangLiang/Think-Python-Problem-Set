import math

def eval_loop():
	content = ''
	while True:
		key = input('Type:\n')
		if key == 'done':
			print(eval(content))
			break
		else:
			print(eval(key))
			content = key

eval_loop()