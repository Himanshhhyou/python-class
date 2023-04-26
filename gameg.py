import random
randomNum = random.randint(1,100)
userInput = int(input("Enter any number between 1 to 100: "))
guess = 1
while  randomNum != userInput:
	if randomNum > userInput:
		print("Guess was too low. TRY AGAIN")
		guess+=1
	elif randomNum < userInput:
		print("Guess was too High. TRY AGAIN")
		guess+=1
	userInput = int(input("Enter any number between 1 to 100: "))
else:
	print("Wow! You guess it in {} attempts.".format(guess))
