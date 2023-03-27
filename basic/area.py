a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
s = (a + b + c) / 2
print("a", a, "b", b, "c", c, )
# 6 * (6-3)*(6-4)*(6-5)
# 6 * 3 *2 *1=36
print((s * (s - a) * (s - b) * (s - c)))
r = (s * (s - a) * (s - b) * (s - c)) ** .5
print("area of triangle ", r)

