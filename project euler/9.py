for a in range(1, 333):
    for b in range(a+1, 500):
        c = (a**2+b**2)**0.5
        if a+b+c == 1000:
            print(int(a*b*c))
            break
