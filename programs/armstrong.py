num = input("Enter the number: ")
temp = num
total = 0
while num > 0:
    lastDigit = temp % 10
    total = total + (lastDigit ** len(str(num)))
    temp = temp // 10
if num == total:
    print(str(num)+" is an armstrong number"))
else:
    print(str(num)+" isn't an armstrong number"))
