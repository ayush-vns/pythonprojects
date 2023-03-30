a, b, c, d, = 12, 13, 14, 15
print(a, b, c, d)
lowest = (a if a < b else a) if a < b else (b if b < d else d) if b < c else (c if c < d else d)
print(lowest)
