# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, 
# print out a message of congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
from random import randint
DB = ["rock","paper","scissors"]
print "Welcome to Rock-Paper-Scissors game \n"
while True:
	str = raw_input("Please shoot: ")
	if(str not in DB):
		print "input is wrong"
	else:
		n = randint(0,2)
		print "the computer shoot: " + DB[n]
		if(str==DB[n]):
			print "TIE, please shoot again"
			continue
		else:
			if(str=="rock" and n==2) or (str=="paper" and n==0) or (str=="scissors" and n==1):
				print "YOU ARE WIN"
				s = raw_input("do you wang to play again (y or n)")
				if(s=='y'):
					continue
				else:
					break
			else:
				print "YOR LOOSE"

				s = raw_input("do you wang to play again (y or n)")
				if(s=='y'):
					continue
				else:
					break