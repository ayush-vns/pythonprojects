a,b,c=7,4,5
print(a,b,c)
if a==b==c:
    print("Equilateral")
elif a==b or a==c or b==c:
    print("Isosceles")
else:
    print("Scalene")