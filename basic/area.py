a = 3
b = 6
c = 7
s = (a + b + c) / 2
print(s)
# 6 * (6-3)*(6-4)*(6-5)
# 6 * 3 *2 *1=36
print((s * (s - a) * (s - b) * (s - c)))
r = (s * (s - a) * (s - b) * (s - c)) ** .5
print(r)
