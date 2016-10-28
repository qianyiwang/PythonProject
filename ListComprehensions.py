# Lets say I give you a list saved in a variable a = 1, 4, 9, 16, 25, 36, 49, 64, 81, 100. 
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
idx = 0
arr = []
arr2 = []
while True:
	v = raw_input("input the %d th element: " %idx)
	if(v=='q'):
		break
	else:
		arr.append(v)
		idx = idx +1
for i in range(len(arr)):
	if((i+1)%2==0):
		arr2.append(arr[i])

print arr2
	