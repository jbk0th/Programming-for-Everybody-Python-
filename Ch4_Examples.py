import random
import math

#for i in range(10):
#	x = random.random()
#	print (x)
	
def print_lyrics():
	print ("I'm a lumberjack, and I'm okay")
	print ("I sleep all night and I work all day")
	
print_lyrics()

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

repeat_lyrics()

def print_twice(bruce):
	print bruce
	print bruce
	
print_twice('Spam')

print_twice('17')

print_twice(math.pi)

print_twice('Spam'*4)

def addtwo(a,b):
	added = a + b
	return added
	
x = addtwo(3,5)
print (x)

