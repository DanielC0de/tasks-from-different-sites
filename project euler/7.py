from sympy import isprime
n = 2
a = []
while len(a) < 10001:
    if isprime(n):
        a.append(n)
        n += 1
    else:
        n += 1
print(max(a))
