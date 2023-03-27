# There are 3 logical operators in Python
"""

and , or , not

and
A       B       output
F       F       F
F       T       F
T       F       F
T       T       T


OR
A       B       Output
F       F       F
F       T       T
T       F       T
T       T       T

Not
A       Output
F       T
T       F
"""
a = False
b = True
print("and ",a and b)
print("or", a or b)
print(not a)
print(not b)
