def is_armstrong(num):
    total = sum(int(digit) ** len(str(num)) for digit in str(num))
    return total == num