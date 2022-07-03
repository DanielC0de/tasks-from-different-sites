a = b = 1
s = 0
# while b != 4000000:
while b <= 4000000:
    a, b = b, a+b
    s += b if b % 2 == 0 else s
print(s)
