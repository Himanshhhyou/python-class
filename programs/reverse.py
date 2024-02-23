num = int(input("Enter the number: "))
reverse = ""
while num > 0:
    lastDigit = num % 10
    reverse = reverse + str(lastDigit)
    num = num // 10
print("After reverse: " + reverse)
