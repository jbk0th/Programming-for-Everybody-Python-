try:	
	hours = input('Enter Hours:\n')
	hours = float(hours)
	rate = input('Enter Rate:\n')
	rate = float(rate)
	if hours > 40:
		overtime = hours - 40
		pay = 40*rate + overtime*(rate*1.5)
	else:
		pay = hours*rate
	pay = str(pay)
	print('Pay: '+pay)
except:
	print('Error, please enter numeric input')