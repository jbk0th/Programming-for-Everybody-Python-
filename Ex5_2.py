total = None
count = 0
largest = None
smallest = None
while True:
	try:
		line = raw_input('Enter a number: ')
		if line == 'done':
			break
		line = float(line)
		if total is None:
			total = line
			smallest = line
			largest = line
		if line < smallest:
			smallest = line
		if line > largest:
			largest = line
		total = total + line
		count = count + 1
	except:
		print('Invalid Input')
print (int(total), int(count), largest, smallest)