# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

list = []
idx = 0
while True:
	l = raw_input("enter the %dth number" %(idx+1))
	if(l!='q' and int(l)<5):
		list.append(l)
		idx = idx+1
	elif(l=='q'):
		print list
		break
	else:
		idx = idx+1

