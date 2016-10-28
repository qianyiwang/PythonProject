# Ask the user for a number and determine whether the number is prime or not

def checkPrimality(num):
	for i in range(num):
		if(i+1)==1 or (i+1)==num:
			continue
		else:
			if num%(i+1)==0:
				return True
			else:
				return False

n = int(raw_input("please input the number you want to check: "))
b = checkPrimality (n)
if b:
	print "It is not a primality number"

else:
	print "It is a primality number"