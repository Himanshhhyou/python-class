![armstrong](img/armstrong.png)
An Armstrong number (also known as a narcissistic number, plenary number, or a plus perfect digital invariant) is a special kind of number in mathematics.<br>
In the case of an n digit number, it is an integer such that the sum of its own digits, each raised to the power of (n), is equal to the number itself.<br><br>
More formally, let's say we have an (n)-digit number (abcd...z). The sum of the (n)-th powers of its digits is:<br>
> a^n + b^n + c^n + ... + z^n = abcd...z

These numbers are named after Michael F. Armstrong, who is credited with discovering them. They have interesting properties and are often used in number theory and recreational mathematics.


## Check the number is armstrong number or not

### By using sun() function
```python
def is_armstrong(num):
    total = sum(int(digit) ** len(str(num)) for digit in str(num))
    return total == num
```

### By using while loop
```python
def is_armstrong(num):
    temp = num
    total = 0
    while temp > 0:
        total += (temp % 10) ** len(str(num))
        temp //= 10
    return total == num
```

### By using For loop
```python
def is_armstrong(num):
    total = 0
    for digit in str(num):
        total += int(digit) ** len(str(num))
    return total == num
```
