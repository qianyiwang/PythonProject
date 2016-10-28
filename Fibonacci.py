# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence 
# is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13

totalLen = int(raw_input("enter the length: "))
fibonnaciArr = []
def fibonnaci(i):
	if i!=totalLen-1:
		if i<2:
			fibonnaciArr.append(1)
		else:
			fibonnaciArr.append(fibonnaciArr[i-2]+fibonnaciArr[i-1])
		i = i+1
		fibonnaci(i)

fibonnaci(0)
print fibonnaciArr

