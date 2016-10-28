# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

idx1 = 0
idx2 = 0
arr1 = []
arr2 = []
while True:
	v = raw_input("please input the %d th number of array1" %(idx1+1))
	if(v=='q'):
		break
	else:
		arr1.append(v)
		idx1 = idx1+1
while True:
	v = raw_input("please input the %d th number of array2" %(idx2+1))
	if(v=='q'):
		break
	else:
		arr2.append(v)
		idx2 = idx2+1

arrOverlap = []
for i in arr1:
	if(i in arr2):
		arrOverlap.append(i)

print arrOverlap