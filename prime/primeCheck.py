def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        return True

for i in range(1,101):
    if i > 1 and is_prime(i):
        print(i,end=' ')