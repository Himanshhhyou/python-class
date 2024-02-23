num = int(input("Enter the number: "))
temp = num
fact = 1
while temp > 0:
    fact = fact * temp
    temp = temp - 1
print("Factorial of  "+str(num)+" is: "+str(fact))
