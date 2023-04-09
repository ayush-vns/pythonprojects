import functools as ft


def mycompare(a, b):
    # Return -ve if a<b, 0 if a==b and +ve if a>b
    # This will sort in reverse order
    if a % 2 == 0:
        return -1
    if b % 2 == 0:
        return 1
    return 0


a = [1, 2, 3, 4, 5]
a.sort(key=ft.cmp_to_key(mycompare))
print(a)

