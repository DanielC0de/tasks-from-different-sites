from sympy import isprime
a = 0
for i in range(1, 2000000):
    if isprime(i):
        a += i
print(a)
