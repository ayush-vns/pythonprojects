a, b, c = 2, 3, 4

high = a if a > b else b
print(high)

high = (a if a > c else c) if a > b else (b if b > c else c)
print(high)
