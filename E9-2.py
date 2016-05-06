fin = open('words.txt')
count = 0
total = 0
for line in fin:
	word = line.strip()
	total = total + 1
	if word.find('e') == -1:
		count = count + 1
		print(word)
print('%.3f' %(100*count/total) + '%')