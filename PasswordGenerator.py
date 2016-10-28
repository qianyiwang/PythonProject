# Write a password generator in Python. 
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, 
# uppercase letters, numbers, and symbols. The passwords should be random, 
# generating a new password every time the user asks for a new password. Include your run-time code in a main method

from random import randint

def generatePassword(length):
	for i in range(length):
		idx = randint(0,len(DB))
		pw.append(DB[idx])
	print ''.join(pw)

if __name__ == '__main__':
	DB = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
	pw = []
	generatePassword(int(raw_input("enter the length of your password")))