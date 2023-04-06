n = 5
"""
row
1 0
2 00
3 000
4 0000
5 00000
c 12345
"""
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(col, end="")
    print()

a = ord('A')
for row in range(1, n + 1):
    for col in range(1, row + 1):
        # ch = chr(a + col - 1)
        ch=a+col-1
        ch=chr(ch)
        print(ch, end="")

    print()
