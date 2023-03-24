a = 1
b = 4
c = -5
discriminant = b * b - 4 * a * c
discriminant = discriminant ** .5
print(discriminant)
r1 = (-b + discriminant) / (2 * a)
r2 = (-b - discriminant) / (2 * a)
print(r1, r2)
