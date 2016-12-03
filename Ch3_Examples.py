#3.1 Boolean Expressions
5 == 5
5 == 6 
x = 1
y = 0
if x > 0:
	print ('x is positive')	
if x > 0:
	pass
if x%2 == 0:
	print('x is even')
else:
	print('x is odd')
if x < y:
	print('x is less than y')
elif x > y:
	print('x is greater than y')
else:
	print('x and y are equal')	
if x > -1 and y > -1:
	print('both x and y are greater than -1')

	
inp = input('Enter Farenheit Temperature:\n')
try:
	fahr = float(inp)
	cel = (fahr - 32.0)* 5.0/9.0
	print (cel)
except:
	print('Please enter a number')

x = input('Enter a value for x:\n')
y = input('Enter a value for y:\n')
x >= 2 and (x/y) > 2
