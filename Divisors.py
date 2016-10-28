# based on the input, return all the divisors
def findDivisors(num):
	list = []
	list1 = range(1,int(num)+1)
	for l in list1:
		if(int(num)%l==0):
			list.append(l)
	return list

num = raw_input("Please input a integer: ")
print findDivisors(num)