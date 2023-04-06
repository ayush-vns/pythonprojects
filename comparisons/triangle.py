a,b,c=7,4,5
print(a,b,c)
if a==b==c:
    print("Equilateral")
elif a==b or a==c or b==c:
    print("Isosceles")
else:
    print("Scalene")

    n = 5
    """
    000000000
    -0000000
    --00000
    ---000
    ----0
    row     space       star
    1        0           9
    2        1           7
    3        2           5
    4        3           3
    5        4           1
    space=1*row-1  
    GfgWinner1
    star=
    """
    for row in range(1, n + 1):
        for space in range(1, n - row + 1):
            print(" ", end="")
        for star in range(1, ):
            print("0", end="")
        print()
