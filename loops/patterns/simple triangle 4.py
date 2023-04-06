n = 4
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
for row in (range(1, n + 1)):
    for space in range(1, n - row + 1):
        print(" ", end="")
    for col in range(1, row + 1):
        print(col, end="")
    for col in range(row - 1, 0, -1):
        print(col, end="")

    print()
a = ord('A')
for row in (range(1, n + 1)):
    for space in range(1, n - row + 1):
        print(" ", end="")
    for col in range(1, row + 1):
        ch = chr(a + col - 1)
        print(ch, end="")
    for col in range(row - 1, 0, -1):
        ch = chr(a + col - 1)
        print(ch, end="")
    print()
