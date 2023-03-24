p = 100
r = 10
t = 5
si = p * r * t / 100
ci = p * (1 + r / 100) ** t - p
print(si, ci)
