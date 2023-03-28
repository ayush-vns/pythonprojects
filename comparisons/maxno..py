a, b, c = 1, 3, 2
print(a, b, c)
if a >= b and a >= c:
    highest = a
    print("a")
elif b >= c:
    highest = b
    print("b")
else:
    highest = c
    print("c")
print(highest)
if a <= b and a <= c:
    lowest = a
    print("a")
elif b <= c:
    lowest = b
    print("b")
else:
    lowest = c
    print("c")
print(lowest)
middle = a + b + c - lowest - highest
print(middle)

if b <= a <= c or c <= a <= b:
    middle = a
elif b >= a and b <= c or b >= c and b <= a:
    middle = b
else:
    middle = c
print(middle)
