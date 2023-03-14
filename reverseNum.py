num = int(input("Enter any number: "))
tempNum = num
reverseNum = 0
while tempNum!=0:
	lastDigit = tempNum%10
	reverseNum =reverseNum*10+lastDigit
	tempNum//=10

print("Reverse of {} is {}".format(num,reverseNum))
