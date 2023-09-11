def is_armstrong(num):
    total = 0
    for digit in str(num):
        total += int(digit) ** len(str(num))
    return total == num