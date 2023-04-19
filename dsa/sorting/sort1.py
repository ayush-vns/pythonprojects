def f(x):
    print("x=", x)
    if x % 2 == 0:
        return 1
    return 0


def f1(x):
    return x[1]


a = [91, 2, 4, 3, 2]
print(a)
a.sort()
print(a)

a.sort(key=f)
print(a)
a = ["ba", "ab", "cat"]
print(a)
a.sort(key=f1)
print(a)

