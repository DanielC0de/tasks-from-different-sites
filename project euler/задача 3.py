num = 600851475143
d = 2
while num != 1 and d*d <= num:
    if num % d == 0:
        num //= d
    else:
        d += 1
print(num)
