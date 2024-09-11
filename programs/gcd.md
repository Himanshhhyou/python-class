## GCD or HCF

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1>num2:
    minNum = num2
else:
    minNum = num1

i = 1
while i<=minNum:
    if (num1%i==0 and num2%i==0):
        gcd = i
    i = i+1
print("GCD is: "+str(gcd))
```