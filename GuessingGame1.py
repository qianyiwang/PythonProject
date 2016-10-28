# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)
# Extras:
# Keep the game going until the user types exit
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
from random import randint
roundNum = 1
res = randint(0,9)
print res
while True:
	str = raw_input("please enter your %d th guess" %roundNum)
	n = int(str)
	if(str=="exit"):
		break
	if(res==n):
		print "EXACTLY RIGHT"
		break
	elif(n<res):
		print "too low"
	elif(n>res):
		print "too high"

