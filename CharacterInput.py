# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
import datetime
for i in range(0,2):
	if i==0:
		name = raw_input("please enter your name: ")
	if i==1:
		age = raw_input("please enter your age: ")


now = datetime.datetime.now()
print "you will turn 100 years old at the year %d" %(now.year+(100-int(age)))
