num = int(input("Enter the number: "))
i = 2
while i < num:
    if num % i == 0:
        print(str(num) + " is not a prime number")
        break
    i+=1
else:
    print(str(num) + " is a prime number")
