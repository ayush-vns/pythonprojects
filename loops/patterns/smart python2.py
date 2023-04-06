n = 7
mid = (n + 1) // 2
for i in range(1, n + 1):
    for j in range(1, n + 1):
        condition = (i==j and i<=mid) or j==1 or j==n
        if condition:
            print("0", end="")
        else:
            print(" ", end="")

    print()









n = 30
mid = (n + 1) // 2
for i in reversed(range(1, n -13)):
    for j in range(1, n + 1):
        condition = (i+j<=n+1) and i<=j
        if condition:
            print(" ", end="")
        else:
            print("0", end="")
    print()
