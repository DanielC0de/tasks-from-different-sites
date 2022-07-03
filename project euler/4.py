
s = []
for i in (i for i in range(999, 99, -1) if i % 10 != 0):
    for n in (j for j in range(i, 99, -1) if j % 10 != 0):
        number = str(i * n)
        if number == number[::-1]:
            s.append(number)
print(max(s))
