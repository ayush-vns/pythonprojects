"""
range(start=1\2, end, step=1\2)
loops up to end-1


"""
r = range(10)
for i in r:
    print(i, end=",")
print()

r = range(1, 11)
for i in r:
    print(i, end=",")
print()

r = range(2, 11, 2)
for i in r:
    print(i, end=",")
print()

r = range(10, 0, -1)
for i in r:
    print(i, end=",")
print()

r = reversed(range(10))
for i in r:
    print(i, end=",")
print()
n = 5

r = range(1, 11)
for i in r:
    print(i * n, end=",")
print()

n = 5
r = range(n, n * 10 + 1, n)
for i in r:
    print(i, end=",")
print()


n=int(input("table="))
r=range(n,n*100+1,n)
for i in r:
    print(i, end="," )
print()





