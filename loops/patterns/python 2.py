n = 15
mid = (n + 1) // 2
for i in (range(1, n + 1)):
    for j in range(1, n + 1):
        condition = (i + j <= mid + 1) or i <= j - 7
        if condition:
            print("0", end="")
        else:
            print(" ", end="")
    print()
