x1 = int(input("x="))
y1 = int(input("y1="))
x2 = int(input("x2="))
y2 = int(input("y2="))
print("x1", x1, "x2", x2, "y1", y1, "y2", y2)
D = (x1 - x2) ** 2 + (y1 - y2) ** 2
distance = D ** .5
print("distance is", distance)
