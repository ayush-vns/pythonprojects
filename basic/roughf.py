for x in range(35, 100):
    i = x * x
    left = i // 100
    l1 = left // 10
    l2 = left % 10
    right = i % 100
    r1 = right // 10
    r2 = right % 10
    if l1 == l2 and r1 == r2:
        print(i, end="\n")
