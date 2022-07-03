c = 0
e = 0
while c != 20:
    c = 0
    e += 2520
    for i in range(1, 21):
        if e % i == 0:
            c += 1
print(e)
