def computepay(hours,rate):
	hours = input('Enter Hours: \n')
	hours = float(hours)
	rate = input('Enter rate: \n')
	rate = float(rate)
	pay = hours*rate
	if hours > 40:
		overtime = hours - 40
		pay = (40*rate) + (rate*1.5)*overtime
	print('Enter Hours: ',hours)
	print('Enter Rate: ',rate)
	print('Pay: ',pay)
	return pay
	
