from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def main():
	import time
	import sys

	from random import randint
	cow = 0
	bull = 0
	round = 0
	cow_position = [0,0,0,0]
	bull_position = [0,0,0,0]
	num = str(randint(1000,9999))

	def delay_print(s, t):
	    for c in s:
	        sys.stdout.write( '%s' % c )
	        sys.stdout.flush()
	        time.sleep(t)

	delay_print("Let's play a game of Cowbull!\n",0.02) #explanation
	delay_print("I will generate a number, and you have to guess the numbers one digit at a time.\n",0.02)
	delay_print("For every number in the wrong place, you get a bull. For every one in the right place, you get a cow.\n",0.05)
	delay_print("The game ends when you get 4 cows!\n",0.02)
	delay_print("Type q at any prompt to exit.\n",0.02)

	while True:
		n = raw_input("please guess a 4-digit number: ")
		if n=='q':
			break
		if n=="show":
			delay_print("HAHA! ARE YOU GIVING UP?",0.1)
			print "The Result is: "+num
			break
		if(len(n)!=4):
			continue

		else:
			round = round +1
			delay_print ("Round %d result \n" %round,0.05)

			for i in range(len(num)):
				if num[i] in n:
					if(n[i]==num[i]):
						cow_position[i] = 1
						bull_position[i] = 0
					else:
						cow_position[i] = 0
						bull_position[i] = n.count(num[i])-cow_position[i]
				else:
					cow_position[i] = 0
					bull_position[i] = 0

			cow = cow_position.count(1)
			bull = sum(bull_position)
			if cow == 4:
				delay_print("YOU GET IT!!!",0.1)
				break
			print "you have %d cow" %cow
			print "you have %d bull" %bull
@application.route("/homepage")
def home():
	return render_template("homepage.html")

@application.route("/hello")
def hello():
	return "Hello Shidi Zhang"

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)