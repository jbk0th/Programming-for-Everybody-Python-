total = None
count = 0
while True:
	try:
		line = raw_input('Enter a number: ')
		if line == 'done':
			break
		if line != 'done':
			line = float(line)
			if total is None:
				total = line
			total = total + line
			count = count + 1
	except:
		print('Invalid Input')
print (int(total), int(count), float(total)/count)