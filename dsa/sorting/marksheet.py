import functools as ft

# math ,chemistry ,physics
import ftplib


def markscompare(s1, s2):
    t1 = s1[0] + s1[1] + s1[2]
    t2 = s2[0] + s2[1] + s2[2]
    return t2 - t1


a = [(9, 3, 4), (5, 8, 9), (8, 9, 7), (2, 7, 9)]
a.sort(key=ft.cmp_to_key(markscompare))

print(a)
