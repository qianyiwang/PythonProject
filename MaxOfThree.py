# Implement a function that takes as input three variables, 
# and returns the largest of the three. Do this without using the Python max() function!
# The goal of this exercise is to think about some internals that Python normally takes care of for us. 
# All you need is some variables and if statements!

var = []
for i in range(0,3):
	print "Please input number %d number" %i
	var.append(raw_input())

max = var[0]
for v in var:
	if(v>max):
		max = v
print max
