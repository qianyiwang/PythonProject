# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

str = raw_input("type the string: ")
strArr = str.split(' ')

for i in range(len(strArr)-1): # do not change the first and last twice
	temp = strArr[i]
	strArr[i] = strArr[len(strArr)-i-1]
	strArr[len(strArr)-i-1] = temp
print "Reverse Word Order is: " + ' '.join(strArr)