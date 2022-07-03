def func(array, num):
    a = []
    for i in array:
        if i % 2 == 0:
            a.append(i)
    for i in range(0, (len(a) - num)):
        a.remove(a[0])
    return a


print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
