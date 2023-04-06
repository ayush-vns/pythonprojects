n = 5
"""
---0
--000
-00000
0000000 

row     space       star
1       4           1
2       3           3
3       2           5
4       1           7

space=n+row
star=2*row-1 
"""
for row in range(1, n + 1):
    for space in range(1, n - row + 1):
        print(" ", end="")
    for star in range(1, row + 1):
        print(star, end="")
    for star in range(row - 1, 0, -1):
        print(star, end="")
    print()