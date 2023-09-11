def is_armstrong(num):
    temp = num
    total = 0
    while temp > 0:
        total += (temp % 10) ** len(str(num))
        temp //= 10
    return total == num