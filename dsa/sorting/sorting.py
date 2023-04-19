def getsum(x):
    # print(x)
    return x[0] + x[1] + x[2]
    # print()


a = [(1, 2, 3), (1, 1, 1), (2, 5, 4), (0, 1, 0)]
print(a)
a.sort(key=getsum)
print(a)
