a,b,c=3,3,3
print(a,b,c)
if a==b==c:
    print("Equilateral")
elif a==b or a==c or b==c:
    print("Isosceles")
else:
    print("Scalene")