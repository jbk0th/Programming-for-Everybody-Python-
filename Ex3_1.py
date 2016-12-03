hours = input('Enter Hours:\n')
rate = input('Enter Rate:\n')
if hours > 40:
	overtime = hours - 40
	pay = 40*rate + overtime*(rate*1.5)
else:
	pay = hours*rate
pay = str(pay)
print('Pay: '+pay)