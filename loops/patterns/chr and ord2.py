n = 5
"""
----0
---00
--000
-0000
00000
row     space       star
1       4           1
2       3           2
3       2           3
4       1           4
5       0           5
space=n-row                                                   
star=row
"""
for row in range(1, n):
    for space in range(1, n - row + 1):
        print(" ", end="")
    for star in range(1, row + 1):
        ch = a + star - 1
        ch = chr(ch)
        print(ch, end="")
    print()
a=ord('A')
for row in reversed(range(1, n + 1)):
    for space in range(1, n - row + 1):
        print(" ", end="")
    for star in range(1, row + 1):
        ch = a + star - 1
        ch = chr(ch)
        print(ch, end="")
    print()

"""
---1
--121
-12321
1234321 
"""