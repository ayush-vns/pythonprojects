n = 7
mid = (n + 1) // 2
for i in range(1, n + 1):
    for j in range(1, n + 1):
        condition = i + j >= mid + 1 and i + j <= n + mid and i - j <= mid - 1 and j - i <= mid - 1 and i <= mid
        if condition:
            print("0", end="")
        else:
            print(" ", end="")

    print()



