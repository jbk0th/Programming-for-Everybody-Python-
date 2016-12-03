n = 5
while n > 0:
	print (n)
	n = n-1
print('Blastoff')

friends = ['Joseph','Glenn','Sally']
for friend in friends:
	print ('Happy New Year',friend)
print ('Done!')

count = 0
for itevar in [3,41,12,9,74,15]:
	count = count + 1
print ('Count', count)

total = 0
for itevar in [3,41,12,9,74,15]:
	total = total + itevar
print ('Total: ', total)

largest = None
print ('Before:', largest)
for itevar in [3,41,12,9,74,15]:
	if largest is None or itevar > largest:
		largest = itevar
	print ('Loop',itevar,largest)
print('Largest:', largest)

smallest = None
print ('Before',smallest)
for itevar in [3,41,12,9,74,15]:
	if smallest is None or itevar < smallest:
		smallest = itevar
	print('Loop',itevar,smallest)
print('Smallest', smallest)
