n = 10
mid = (n + 1) // 2
for i in reversed(range(1, n + 1)):
    for j in range(1, n + 1):
        condition =i<=j
        if condition:
            print("0", end="   ")
        else:
            print("", end="")
    print()
