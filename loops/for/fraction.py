n = 10
# n = int(input("no."))
r = range(1, n + 1)
for i in r:
    # print(1/i, end=",")
    print("1 /", i, end=",")
print()

# n = int(input("no."))
r = range(1, n + 1)
for i in r:
    print(i * i, end=",")
print()

# n = int(input("no."))
r = range(2,n+1)
for i in r:
    print(i*(i-1), end=",")
print()


r = reversed(range(2,n+1))
for i in r:
    print(i*(i-1), end=",")
print()


r = reversed(range(1, n + 1))
for i in r:
    print(i * i, end=",")
print()

n=int(input("number="))
r=range(n,n*10+1,n)
for i in r:
    print(i,end=",")
