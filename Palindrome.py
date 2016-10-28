# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same #forwards and backwards.)

str = raw_input("input string: ")
for i in range(len(str)):
	if(str[i]==str[len(str)-i-1]):
		if(i==len(str)-1):
			print "the string is palindrome"
		continue
	else:
		print("the string is not palindrome")
		break

