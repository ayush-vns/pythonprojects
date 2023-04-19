import functools as ft


def datecompare(d1, d2):
    # Return -ve if d1<d2, 0 if d1==d2 and +ve if d1>d2
    y1 = d1[2]
    y2 = d2[2]
    if y1 < y2:
        return -1
    if y1 > y2:
        return 1
    m1 = d1[1]
    m2 = d2[1]
    if m1 < m2:
        return -1
    if m1 > m2:
        return 1
    dt1 = d1[0]
    dt2 = d2[0]
    if dt1 < dt2:
        return -1
    if dt1 > dt2:
        return 1
    return 0


a = [(1, 2, 1946), (14, 2, 1946), (15, 2, 1946), (31, 22, 1946)]
a.sort(key=ft.cmp_to_key(datecompare))

print(a)
