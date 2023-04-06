n = 4
"""
row
1 0
2 00
3 000
4 0000
5 00000
6 000000
c 123456
"""
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print("0", end="")
    print()
"""
---0
--00
-000
0000

n=4
row     space       star
1       3           1
2       2           2
3       1           3
4       0           4

space=n-row
star=row
"""
for row in range(1, n + 1):
    for space in range(1, n - row + 1):
        print(" ", end="")
    for star in range(1, row + 1):
        print("0", end="")
    print()

for row in reversed(range(1, n + 1)):
    for space in range(1, n - row + 1):
        print(" ", end="")
    for star in range(1, row + 1):
        print("0", end="")
    print()
