num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1>num2:
	min = num2
else:
	min = num1

for i in range(1,min+1):
	if num1%i==0 and num2%i==0:
		gcd = i
print("GCD of {} and {} is {}".format(num1,num2,gcd))

