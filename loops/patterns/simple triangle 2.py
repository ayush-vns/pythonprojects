n=5
"""
----0
---000
--00000
-0000000
000000000

row     space       star
1       4           1
2       3           3
3       2           5
4       1           7
5       0           9

space=n+row
star=2*row-1 2x1-1=1, 2x2-1=4-1=3
"""
for row in range(1, n+1  ):
    for space in range(1, n - row +1):
        print(" ", end="")
    print()
    for star in range(1, 2*row ):
        print("0", end="")
    print()


for row in reversed(range(1, n )):
    for space in range(1, n - row + 1):
        print(" ", end="")
    for star in range(1, 2*row ):
        print("0", end="")
    print()
